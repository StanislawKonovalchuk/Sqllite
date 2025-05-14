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