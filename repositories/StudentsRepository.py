from sqlalchemy.orm import Session
from Models import Student

class StudentRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, student_id: int) -> Student | None:
        return self.db.query(Student).filter(Student.id == student_id).first()

    def get_by_username(self, name: str) -> Student | None:
        return self.db.query(Student).filter(Student.name == name).first()

    def get_all(self) -> list[Student]:
        return self.db.query(Student).all()

    def create(self, student: Student) -> Student:
        self.db.add(student)
        self.db.commit()
        self.db.refresh(student)
        return student

    def delete(self, student_id: int) -> bool:
        student = self.get_by_id(student_id)
        if student:
            self.db.delete(student)
            self.db.commit()
            return True
        return False