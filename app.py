from flask import Flask
from src.resources import resources_blueprint
from src.recommender import recommender_blueprint

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def hello():
    return "Hello!"

app.register_blueprint(resources_blueprint, url_prefix='/resources')
app.register_blueprint(recommender_blueprint, url_prefix='/recommender')

if __name__ == "__main__":
    app.run()