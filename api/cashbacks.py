from flask_jwt import jwt_required

from api import api
import requests


@api.route('/cashbacks/<string:cpf>', methods=['GET'])
@jwt_required()
def get_cashbacks(cpf):
    headers = {'token': 'ZXPURQOARHiMc6Y0flhRC1LVlZQVFRnm'}
    params = {'cpf': cpf}
    return requests.get('https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback',
                        params=params,
                        headers=headers).content
