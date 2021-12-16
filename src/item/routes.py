from flask import Blueprint, request, jsonify
from os import environ

import src.utils.bucket as bc

from ..services.user_service import insert_user_dict

item_blueprint = Blueprint('item', __name__)

@item_blueprint.route('/user', methods=['POST'])
def teste():

    data = request.json

    return { 'user_id': insert_user_dict(data['user']) }

@item_blueprint.route('/', methods=['GET'])
def init():

    movies_data = bc.read_csv(environ['MOVIES_FILE'])

    return jsonify(movies_data.sample(n=9).to_dict(orient='records'))

@item_blueprint.route('/search', methods=['GET'])
def search():
    title = request.args.get('title')

    movies_data = bc.read_csv(environ['MOVIES_FILE'])

    movies_data_titles = movies_data['title'].str.lower()

    movies_data_titles = movies_data_titles.str.contains(title.lower())

    return jsonify(movies_data[movies_data_titles].to_dict(orient='records'))