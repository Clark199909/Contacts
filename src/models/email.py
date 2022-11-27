from src import db
from src.models.email_type import EmailType


class Email(db.Model):
    __tablename__ = 'email'

    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer, db.ForeignKey('email_type.id'), nullable=False)
    uni = db.Column(db.Integer, db.ForeignKey('student.uni'), nullable=False)
    address = db.Column(db.String(50), nullable=False)

    email_type = db.relationship("EmailType")
