from sqlalchemy import String, Integer, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from .Base import Base

class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    age: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
   
    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name}, email={self.email}, age={self.age})>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.name,
            'email': self.email,
            'age': self.age,
            'created_at': self.created_at.isoformat()
        }