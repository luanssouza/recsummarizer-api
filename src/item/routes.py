from flask import Blueprint, request, jsonify
import pandas as pd

item_blueprint = Blueprint('item', __name__)

@item_blueprint.route('/', methods=['GET'])
def init():

    movies_file = ''

    movies_data = pd.read_csv(movies_file)

    return jsonify(movies_data.sample(n=9).to_dict(orient='records'))

@item_blueprint.route('/search', methods=['GET'])
def search():
    title = request.args.get('title')

    movies_file = ''

    movies_data = pd.read_csv(movies_file)

    movies_data_titles = movies_data['title'].str.lower()

    movies_data_titles = movies_data_titles.str.contains(title.lower())

    return jsonify(movies_data[movies_data_titles].to_dict(orient='records'))