from flask import Blueprint
from flask_jwt import JWT
from utils.authentication import authenticate, identity
from app import app

api = Blueprint('api', __name__)

jwt = JWT(app, authenticate, identity)

from api import cashbacks
from api import purchases
from api import resellers
