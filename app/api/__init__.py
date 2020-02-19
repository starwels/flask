from flask import Blueprint

api = Blueprint('api', __name__)

from app.api import purchases
from app.api import resellers
