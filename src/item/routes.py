from flask import Blueprint, request, jsonify
import pandas as pd

item_blueprint = Blueprint('item', __name__)

@item_blueprint.route('/search', methods=['GET'])
def search():
    title = request.args.get('title')

    movies_file = ''

    movies_data = pd.read_csv(movies_file)

    return jsonify(movies_data[movies_data['title'].str.contains(title)].to_dict(orient='records'))