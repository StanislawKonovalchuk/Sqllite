from service import StudentService
from Models import Base
from database import engine
from flask import request

class StudentController:
    def __init__(self, app):
        self.service = StudentService()
        app.add_url_rule('/students', view_func=self.get_student, methods=['GET'])
        app.add_url_rule('/students/add', view_func=self.post_student, methods=['POST'])

    def get_student(self):
        id = int(request.args.get('id'))
        return self.service.get_by_id_student(id).to_dict()

    def post_student(self):
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        age = data.get('age')
        return self.service.add_student(name, email, age).to_dict()