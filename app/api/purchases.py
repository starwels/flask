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
        'purchases': purchases
    })


@api.route('/purchases/<int:id>', methods=['GET'])
def get_purchase(id):
    purchase = Purchase.query.get_or_404(id)
    current_app.logger.info('Retrieving purchase {}'.format(id))
    return purchase


@api.route('/purchases/', methods=['POST'])
def new_purchase():
    purchase = Purchase.from_json(request.json)
    current_app.logger.info('Creating new purchase')
    db.session.add(purchase)
    db.session.commit()
    return purchase, 201

