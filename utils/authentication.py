from werkzeug.security import safe_str_cmp
from models.resellers import Reseller


def authenticate(cpf, password):
    reseller = Reseller.find_by_cpf(cpf)
    if reseller and safe_str_cmp(reseller.password, password):
        return reseller


def identity(payload):
    reseller_id = payload['identity']
    return Reseller.find_by_id(reseller_id)
