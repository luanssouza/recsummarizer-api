import numpy as np
import pandas as pd
from flask import Blueprint, request
from os import environ

from src.summarizer.proposal import SummarizerClusters

from .proposal.summarizer_clusters_semantic import SummarizerClustersSemantic

from ..services.compare_service import insert_compare_dict
from ..services.explanation_service import insert_explanation_dict
from ..services.tries_service import insert_tries_dict

from ..utils.bucket import read_numpy

summarizer_blueprint = Blueprint('summarizer', __name__)

@summarizer_blueprint.route('/explain', methods=['POST'])
def explain():
    data = request.json

    explanations = environ['EXPLANATIONS']

    exp_df = pd.read_csv(explanations, index_col = 'movie_id')
    
    explanation = exp_df.loc[data['movie_id']][data['n_clusters']]

    return { 'explanation': explanation }

@summarizer_blueprint.route('/baseline', methods=['POST'])
def baseline():
    data = request.json

    explanations = environ['EXPLANATIONS_BASELINE']

    exp_df = pd.read_csv(explanations, index_col = 'movie_id')

    explanation = exp_df.loc[data['movie_id']]['summary']

    return { 'explanation': explanation }

@summarizer_blueprint.route('/summarize', methods=['POST'])
def summarize():
    data = request.json

    movie_id = int(data['movie_id'])
    n_clusters = int(data['n_clusters'])

    sentences_path_bert = environ['EXPLANATIONS_FILES']

    summary = ''

    if data['rates']:
        user_itens = [d['movie_id'] for d in data['rates']]

        asp_cen = sum([read_numpy(f'{environ["MOVIE_CENTROIDS"]}/{i}_centroid.npy') for i in user_itens])

        summarizer_bert = SummarizerClustersSemantic(sentences_path_bert, 0.9, 5)

        summary = summarizer_bert.summarize(movie_id, n_clusters, asp_cen)

    else:
        summarizer_bert = SummarizerClusters(sentences_path_bert)

        summary = summarizer_bert.summarize(movie_id, n_clusters)

    return { "explanation": ' '.join(summary) }

@summarizer_blueprint.route('/evaluation', methods=['POST'])
def evaluation():
    data = request.json

    insert_explanation_dict(data['evaluation'])

    return {"message": "created"}, 201

@summarizer_blueprint.route('/tries', methods=['POST'])
def tries():
    data = request.json

    insert_tries_dict(data['tries'])

    return {"message": "created"}, 201

@summarizer_blueprint.route('/compare', methods=['POST'])
def compare():
    data = request.json

    insert_compare_dict(data['compare'])

    return {"message": "created"}, 201
