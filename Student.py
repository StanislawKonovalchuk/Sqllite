from service import StudentService
from Models import Base
from database import engine

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

    service = StudentService()
    student = service.add_student("admin", "admin@example.com", 21)
    print(student)