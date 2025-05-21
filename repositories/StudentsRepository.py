from sqlalchemy.orm import Session
from Models import Student

class StudentRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, student_id: int) -> Student | None:
        return self.db.query(Student).filter(Student.id == student_id).first()

    def get_by_name(self, name: str) -> Student | None:
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
    
    def update(self, student_id: int, name: str = None, email: str = None, age: int = None) -> Student | None:
        student = self.get_by_id(student_id)
        if student:
            student.name = name
            student.email = email
            student.age = age
            self.db.commit()
            self.db.refresh(student)
            return student
        return None