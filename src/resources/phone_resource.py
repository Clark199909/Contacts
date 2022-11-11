from src import db
from src.models.phone import Phone
from src.models.phone_type import PhoneType


class PhoneResource:
    def __int__(self):
        pass

    @staticmethod
    def add_new_phone(type_id, uni, country_code, phone_no):
        phone = Phone(type_id=type_id, uni=uni, country_code=country_code, phone_no=phone_no)
        db.session.add(phone)
        db.session.commit()

    @staticmethod
    def search_phone_by_type_id_and_uni(type_id, uni):
        return db.session.query(Phone).filter_by(type_id=type_id, uni=uni).first()

    @staticmethod
    def search_type_id(description):
        return db.session.query(PhoneType.id).filter_by(description=description).first()
