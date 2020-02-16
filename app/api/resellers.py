from flask import jsonify, request, current_app
from app.models.resellers import Reseller
from app.api import api
from app import db


@api.route('/resellers/', methods=['GET'])
def get_resellers():
    current_app.logger.info('Retrieving all resellers')
    current_app.logger.debug('This is a debug log')
    resellers = Reseller.query.all()
    return jsonify({
        'resellers': resellers
    })


@api.route('/resellers/<int:id>', methods=['GET'])
def get_reseller(id):
    reseller = Reseller.query.get_or_404(id)
    current_app.logger.info('Retrieving reseller {}'.format(id))
    return reseller


@api.route('/resellers/', methods=['POST'])
def new_reseller():
    reseller = Reseller.from_json(request.json)
    current_app.logger.info('Creating new reseller')
    db.session.add(reseller)
    db.session.commit()
    return reseller, 201

