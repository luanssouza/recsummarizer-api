from werkzeug.exceptions import HTTPException
from flask import Blueprint
import logging

error_blueprint = Blueprint('error_handler', __name__)

@error_blueprint.app_errorhandler(Exception)
def handle_exception(e):
    logging.error(e)
    
    if isinstance(e, HTTPException):
        return e

    return { "message" : "Internal Server Error!", "status": 500 }, 500