from flask import Blueprint, request
from os import environ

from src.summarizer.proposal import SummarizerClusters

summarizer_blueprint = Blueprint('summarizer', __name__)

@summarizer_blueprint.route('/explain', methods=['POST'])
def explain():
    data = request.json

    explanations_path = environ['EXPLANATIONS']

    explanation = open(f'{explanations_path}{data["movie_id"]}/{data["n_clusters"]}.txt', 'r').read()

    return { 'explanation': explanation }

@summarizer_blueprint.route('/baseline', methods=['POST'])
def baseline():
    data = request.json

    explanations_path = environ['EXPLANATIONS_BASELINE']

    explanation = open(f'{explanations_path}{data["movie_id"]}.txt', 'r').read()

    return { 'explanation': explanation }

@summarizer_blueprint.route('/summarize', methods=['POST'])
def summarize():
    data = request.json

    sentences_path_bert = ''

    summarizer_bert = SummarizerClusters(sentences_path_bert)

    explanation = " ".join(summarizer_bert.summarize(int(data['movie_id']), int(data['n_clusters'])))

    return { "explanation": explanation }