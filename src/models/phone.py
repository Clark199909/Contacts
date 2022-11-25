from src import db
from src.models.phone_type import PhoneType


class Phone(db.Model):
    __tablename__ = 'phone'

    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer, db.ForeignKey('phone_type.id'), nullable=False)
    uni = db.Column(db.Integer, db.ForeignKey('student.uni'), nullable=False)
    country_code = db.Column(db.String(10), nullable=False)
    phone_no = db.Column(db.String(20), nullable=False)

    phone_type = db.relationship("PhoneType")
