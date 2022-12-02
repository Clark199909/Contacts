from src import db


class AddressType(db.Model):
    __tablename__ = 'address_type'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50), nullable=False)
