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

    def to_json(self):
        reseller = {
            'id': self.id,
            'name': self.name,
            'cpf': self.cpf,
            'email': self.email,
            'password': self.password,
        }
        return reseller

    @staticmethod
    def from_json(json_post):
        name = json_post.get('name')
        cpf = json_post.get('cpf')
        email = json_post.get('email')
        password = json_post.get('password')

        reseller = Reseller(
            name=name,
            cpf=cpf,
            email=email,
            password=password
        )
        return reseller

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        self.cpf.replace('.', '')
        self.cpf.replace('-', '')

        db.session.add(self)
        db.session.commit()
