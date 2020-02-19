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

    @classmethod
    def find_by_cpf(cls, cpf):
        return cls.query.filter_by(cpf=cpf).first()

    def to_json(self):
        purchase = {
            'id': self.id,
            'code': self.code,
            'value': self.value,
            'date': self.date,
            'cpf': self.cpf,
            'status': self.status,
        }
        return purchase

    @staticmethod
    def from_json(json_post):
        code = json_post.get('code')
        value = json_post.get('value')
        date = json_post.get('date')
        cpf = json_post.get('cpf')
        status = json_post.get('status')

        purchase = Purchase(
            code=code,
            value=value,
            date=date,
            cpf=cpf,
            status=status
        )
        return purchase

    def save_to_db(self):
        if self.cpf == '15350946056':
            self.status = 'Aprovado'

        self.cpf.replace('.', '')
        self.cpf.replace('-', '')

        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
