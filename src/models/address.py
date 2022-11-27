from src import db
from src.models.address_type import AddressType


class Address(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer, db.ForeignKey('address_type.id'), nullable=False)
    uni = db.Column(db.Integer, db.ForeignKey('student.uni'), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    zip_code = db.Column(db.String(10), nullable=False)
    street = db.Column(db.String(100), nullable=False)

    address_type = db.relationship('AddressType')
