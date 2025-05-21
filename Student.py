from Controler import StudentController
from Models import Base
from database import engine
from flask import Flask

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

app = Flask(__name__)
controller = StudentController(app)
app.run(debug=True)