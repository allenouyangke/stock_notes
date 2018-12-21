from flask import Blueprint

baseStock = Blueprint('baseStock', __name__)

from . import main