from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from flask_cors import CORS

# App Modules
from src.error import error_blueprint
from src.recommender import recommender_blueprint
from src.summarizer import summarizer_blueprint
from src.item import item_blueprint

app = Flask(__name__)
CORS(app)

@app.route("/", methods = ['GET'])
def hello():
    return "Hello!"

app.register_blueprint(error_blueprint)

app.register_blueprint(recommender_blueprint, url_prefix='/recommender')
app.register_blueprint(summarizer_blueprint, url_prefix='/summarizer')
app.register_blueprint(item_blueprint, url_prefix='/item')

if __name__ == "__main__":
    app.run()