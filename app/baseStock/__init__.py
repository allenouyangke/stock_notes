from flask import Blueprint

auth = Blueprint('baseStock', __name__)

from . import main