from flask import jsonify, request, current_app
from models.purchases import Purchase
from api import api
from flask_jwt import jwt_required, current_identity


@api.route('/purchases/', methods=['GET'])
@jwt_required()
def get_purchases():
    current_app.logger.info(current_identity)
    current_app.logger.info('Retrieving all purchases')
    current_app.logger.debug('This is a debug log')
    purchases = Purchase.query.all()
    return jsonify({
        'purchases': [purchase.to_json() for purchase in purchases]
    })


@api.route('/purchases/', methods=['POST'])
@jwt_required()
def new_purchase():
    purchase = Purchase.from_json(request.json)
    current_app.logger.info('Creating new purchase')
    purchase.save_to_db()
    return jsonify(purchase.to_json()), 201
