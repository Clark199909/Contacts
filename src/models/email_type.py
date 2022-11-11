from src import db


class EmailType(db.Model):
    db.__tablename__ = 'email_type'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50), nullable=False)
