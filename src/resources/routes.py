from flask import Blueprint, send_file

resources_blueprint = Blueprint('resources', __name__)

@resources_blueprint.route('/tcle', methods=['GET'])
def tcle():
    return send_file('static/TCLE.pdf', attachment_filename='TCLE.pdf')