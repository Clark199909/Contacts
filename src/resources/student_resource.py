from src import db
from src.models.student import Student

class StudentResource:
    def __int__(self):
        pass

    @staticmethod
    def search_student_by_uni(uni):
        return db.session.query(Student).filter_by(uni=uni).first()

    @staticmethod
    def del_a_student(uni):
        student = db.session.query(Student).filter_by(uni=uni).first()
        db.session.delete(student)
        db.session.commit()
