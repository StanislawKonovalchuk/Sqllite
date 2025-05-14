from service import StudentService
from Models import Base
from database import engine

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

    service = StudentService()
    students = service.get_all_student()
    for student in students:
        print(student)