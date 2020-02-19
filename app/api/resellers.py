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
        'resellers': [reseller.to_json() for reseller in resellers]
    })


@api.route('/resellers/<int:id>', methods=['GET'])
def get_reseller(id):
    reseller = Reseller.query.get_or_404(id)
    current_app.logger.info('Retrieving reseller {}'.format(id))
    return jsonify(reseller.to_json())


@api.route('/resellers/', methods=['POST'])
def new_reseller():
    reseller = Reseller.from_json(request.json)
    current_app.logger.info('Creating new reseller')
    db.session.add(reseller)
    db.session.commit()
    return jsonify(reseller.to_json()), 201


@api.route('/resellers/<int:id>', methods=['PUT'])
def edit_story(id):
    reseller = Reseller.query.get_or_404(id)
    reseller.name = request.json.get('name')
    reseller.cpf = request.json.get('cpf')
    reseller.email = request.json.get('email')
    reseller.password = request.json.get('password')

    current_app.logger.info('Editing reseller {}'.format(id))
    db.session.add(reseller)
    db.session.commit()
    return jsonify(reseller.to_json())

