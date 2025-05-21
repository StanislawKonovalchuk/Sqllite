from repositories import StudentRepository
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models import Student
from database import SessionLocal

class StudentService:
    def __init__(self):
        self.repository = StudentRepository(SessionLocal())

    def add_student(self, name: str, email: str, age: int) -> Student | None:
        if name.strip() and email.strip():
            student = Student(name=name, email=email, age=age)
            return self.repository.create(student)
        return None
    
    def daleted_student(self, id: int) -> Student | None:
        if id != 0:
            return self.repository.delete(id)
        return None
    
    def get_by_id_student(self, id: int) -> Student | None:
        if id != 0:
            return self.repository.get_by_id(id)
        return None
    
    def get_by_name_student(self, name: str) -> Student | None:
        if name.strip:
            return self.repository.get_by_name(name)
        return None
    
    def get_all_student(self)-> list[Student]:
        return self.repository.get_all()
    
    def update_student(self, id: int, name: str = None, email: str = None, age: int = None) -> Student | None:
        if id != 0 and name.strip() and email.strip():
            return self.repository.update(id, name=name, email=email, age=age)
        return None