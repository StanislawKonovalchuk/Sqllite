from sqlalchemy import create_engine, Column, Integer, String, TEXT
from sqlalchemy.orm import DeclarativeBase, sessionmaker


DATABASE_URL = "sqlite:///test.db"

engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine, autoflush=False)

class Base(DeclarativeBase): pass
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(TEXT(40), nullable=False)

Base.metadata.create_all(bind=engine)

with Session(autoflush=False, bind=engine) as db:
    Egor= Student(name="Egor", age= 21, email= "egorchev@gmail.com")
    db.add(Egor)
    db.commit()