from src import db
from src.models.student import Student


class StudentResource:
    def __int__(self):
        pass

    @staticmethod
    def add_new_student(uni):
        student = Student(uni=uni)
        db.session.add(student)
        db.session.commit()

    @staticmethod
    def search_student_by_uni(uni):
        return db.session.query(Student).filter_by(uni=uni).first()
