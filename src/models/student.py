from src import db
from src.models.email import Email
from src.models.address import Address
from src.models.phone import Phone


class Student(db.Model):
    db.__tablename__ = 'student'

    uni = db.Column(db.String(10), primary_key=True)

    emails = db.relationship('Email', backref='student')
    addresses = db.relationship('Address', backref='student')
    phones = db.relationship('Phone', backref='student')
