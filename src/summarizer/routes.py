from flask import Blueprint, request
import pandas as pd
import numpy as np

from src.summarizer.proposal import SummarizerClusters

summarizer_blueprint = Blueprint('summarizer', __name__)

@summarizer_blueprint.route('/explain', methods=['POST'])
def explain():
    data = request.json

    sentences_path_bert = ''

    summarizer_bert = SummarizerClusters(sentences_path_bert)

    explanation = " ".join(summarizer_bert.summarize(data['movie_id'], data['n_clusters']))

    return { "explanation": explanation }