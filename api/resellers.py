from flask import jsonify, request, current_app
from flask_jwt import jwt_required

from models.resellers import Reseller
from api import api


@api.route('/resellers/', methods=['POST'])
@jwt_required()
def new_reseller():
    reseller = Reseller.from_json(request.json)

    if Reseller.find_by_cpf_and_email(reseller.cpf, reseller.email):
        return {'message': "Um vendedor com esse cpf ou email já existe."}, 400

    current_app.logger.info('Creating new reseller')
    reseller.save_to_db()
    return jsonify(reseller.to_json()), 201

