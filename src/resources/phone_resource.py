from src import db
from src.models.phone import Phone
from src.models.phone_type import PhoneType
from src.models.student import Student


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

    @staticmethod
    def search_all_phones_of_a_student(uni):
        res = db.session.query(Student).filter_by(uni=uni).first()
        if res is None:
            return {}

        phones = res.phones
        phone_list = []
        PhoneResource.parse_phone_info(phones, phone_list)
        return phone_list

    @staticmethod
    def search_all_phones_of_all_students():
        students = db.session.query(Student).all()

        phone_list = []
        for student in students:
            phones = student.phones
            PhoneResource.parse_phone_info(phones, phone_list)

        return phone_list

    @staticmethod
    def parse_phone_info(phones, phone_list):

        for phone in phones:
            phone_dict = {'id': phone.id,
                          'uni': phone.uni,
                          'country_code': phone.country_code,
                          'phone_no': phone.phone_no,
                          'phone_type': phone.phone_type.description}
            phone_list.append(phone_dict)
