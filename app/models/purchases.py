from app import db


class Purchase(db.Model):
    __tablename__ = 'purchases'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(80))
    value = db.Column(db.String(11))
    date = db.Column(db.DateTime())
    cpf = db.Column(db.String(11))
    status = db.Column(db.String(20), default='Em validação')

    reseller_cpf = db.Column(db.String(11), db.ForeignKey('resellers.cpf'))
    reseller = db.relationship('Reseller')

    def __init__(self, **kwargs):
        super(Purchase, self).__init__(**kwargs)
