from flask import jsonify, request, current_app
from app.models.purchases import Purchase
from app.api import api
from app import db


@api.route('/purchases/', methods=['GET'])
def get_purchases():
    current_app.logger.info('Retrieving all purchases')
    current_app.logger.debug('This is a debug log')
    purchases = Purchase.query.all()
    return jsonify({
        'purchases': [purchase.to_json() for purchase in purchases]
    })


@api.route('/purchases/<int:id>', methods=['GET'])
def get_purchase(id):
    purchase = Purchase.query.get_or_404(id)
    current_app.logger.info('Retrieving purchase {}'.format(id))
    return jsonify(purchase.to_json())


@api.route('/purchases/', methods=['POST'])
def new_purchase():
    purchase = Purchase.from_json(request.json)
    current_app.logger.info('Creating new purchase')
    purchase.save_to_db()
    return jsonify(purchase.to_json()), 201


@api.route('/purchases/<int:id>', methods=['PUT'])
def edit_purchase(id):
    purchase = Purchase.query.get_or_404(id)
    purchase.code = request.json.get('code')
    purchase.value = request.json.get('value')
    purchase.date = request.json.get('date')
    purchase.reseller_cpf = request.json.get('reseller_cpf')

    current_app.logger.info('Editing purchase {}'.format(id))
    purchase.save_to_db()
    return jsonify(purchase.to_json())
