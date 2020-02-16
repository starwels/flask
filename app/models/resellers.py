from app import db


class Reseller(db.Model):
    __tablename__ = 'resellers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    cpf = db.Column(db.String(11), unique=True)
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(255))

    def __init__(self, **kwargs):
        super(Reseller, self).__init__(**kwargs)

    @classmethod
    def find_by_cpf(cls, cpf):
        return cls.query.filter_by(cpf=cpf).first()
