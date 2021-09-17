from flask import Blueprint, request
import pandas as pd
import numpy as np

from src.recommender.collaborative import UserKnn

recommender_blueprint = Blueprint('recommender', __name__)

@recommender_blueprint.route('/recommendation', methods=['POST'])
def recommendation():
    data = request.json

    train_file = ''

    names = ['user_id', 'movie_id', 'rating']
    header = None
    sep = "\t"

    train = pd.read_csv(train_file, header = header, names = names, sep=sep)

    movies_file = ''

    movies_data = pd.read_csv(movies_file, index_col="movie_id")

    user_id = train['user_id'].max()+1

    user_interactions = data

    for interaction in user_interactions:
        interaction['user_id'] = user_id
        interaction['movie_id'] = int(interaction['movie_id'])
        interaction['rating'] = float(interaction['rating'])


    train = train.append(user_interactions, ignore_index = True)

    user_knn = UserKnn(train.drop_duplicates(subset=['user_id', 'movie_id'], keep='last'))

    recommended_user_knn = user_knn.recommend(user_id, 2)

    return movies_data.loc[recommended_user_knn[0][0]].to_dict()