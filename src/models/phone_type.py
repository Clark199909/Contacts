from src import db


class PhoneType(db.Model):
    __tablename__ = 'phone_type'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50), nullable=False)
