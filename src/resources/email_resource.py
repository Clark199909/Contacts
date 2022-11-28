from src import db
from src.models.email import Email
from src.models.email_type import EmailType
from src.models.student import Student


class EmailResource:
    def __int__(self):
        pass

    @staticmethod
    def add_new_email(type_id, uni, address):
        email = Email(type_id=type_id, uni=uni, address=address)
        db.session.add(email)
        db.session.commit()

    @staticmethod
    def search_email_by_type_id_and_uni(type_id, uni):
        return db.session.query(Email).filter_by(type_id=type_id, uni=uni).first()

    @staticmethod
    def search_type_id(description):
        return db.session.query(EmailType.id).filter_by(description=description).first()

    @staticmethod
    def search_all_emails_of_a_student(uni):
        res = db.session.query(Student).filter_by(uni=uni).first()
        if res is None:
            return {}

        emails = res.emails
        email_list = []
        EmailResource.parse_email_info(emails, email_list)
        return email_list

    @staticmethod
    def search_all_email_of_all_students():
        students = db.session.query(Student).all()

        email_list = []
        for student in students:
            emails = student.emails
            EmailResource.parse_email_info(emails, email_list)

        return email_list

    @staticmethod
    def del_an_email_by_uni_and_type(type_id, uni):
        email = db.session.query(Email).filter_by(type_id=type_id, uni=uni).first()
        db.session.delete(email)
        db.session.commit()

    @staticmethod
    def update_an_email_by_uni_and_type(type_id, uni, address):
        email = db.session.query(Email).filter_by(type_id=type_id, uni=uni).update({"address": address})
        db.session.commit()

    @staticmethod
    def del_all_emails_of_a_student(uni):
        student = db.session.query(Student).filter_by(uni=uni).first()
        emails = student.emails
        for email in emails:
            db.session.delete(email)
            db.session.commit()

    @staticmethod
    def parse_email_info(emails, email_list):

        for email in emails:
            email_dict = {'id': email.id,
                            'uni': email.uni,
                            'address': email.address,
                            'email_type': email.email_type.description}
            email_list.append(email_dict)
