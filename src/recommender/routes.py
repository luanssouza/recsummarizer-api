from flask import Blueprint, request
from os import environ

import src.utils.bucket as bc
from src.recommender.collaborative import UserKnn

from ..services.recommendation_service import insert_recommendation_dict

recommender_blueprint = Blueprint('recommender', __name__)

@recommender_blueprint.route('/recommendation', methods=['POST'])
def recommendation():
    data = request.json

    names = ['user_id', 'movie_id', 'rating']
    header = None
    sep = "\t"

    train = bc.read_csv(environ['RATINGS_FILE'], header = header, names = names, sep=sep)

    movies_data = bc.read_csv(environ['MOVIES_FILE'], index_col="movie_id")

    user_id = train['user_id'].max()+1

    user_interactions = []

    for rate in data['rates']:
        interaction = {}
        interaction['user_id'] = user_id
        interaction['movie_id'] = int(rate['movie_id'])
        interaction['rating'] = float(rate['rating'])
        user_interactions.append(interaction)

    train = train.append(user_interactions, ignore_index = True)

    user_knn = UserKnn(train.drop_duplicates(subset=['user_id', 'movie_id'], keep='last'))

    recommended_user_knn = user_knn.recommend(user_id, 2)

    recommended = movies_data.loc[recommended_user_knn[0][0]].to_dict()

    recommended["movie_id"] = recommended_user_knn[0][0]

    data['movie_id'] = recommended["movie_id"]

    insert_recommendation_dict(data)

    return recommended