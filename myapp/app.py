from flask import Flask
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)

STUDENTS = {
    '1': {'firstname': 'Michal', 'lastname': 'Zborovsky'},
    '2': {'firstname': 'Ben', 'lastname': 'Goldenberg'},
    '3': {'firstname': 'Gal', 'lastname': 'Shmolivish'},
    '4': {'firstname': 'Avigail', 'lastname': 'Spektor'},
    '5': {'firstname': 'Adi', 'lastname': 'Zalmanovich'}
 }

parser = reqparse.RequestParser()

class StudentsList(Resource):
     def get(self):
         return STUDENTS


     def post(self):
         parser.add_argument("firstname")
         parser.add_argument("lastname")
         args = parser.parse_args()
         students_id = int(max(STUDENTS.keys())) +1
         students_id = '%i' % students_id
         STUDENTS[students_id] = {
             "firstname": args["firstname"],
            "lastname":args["lastname"],
         }
         return STUDENTS[students_id],201

class Student(Resource):

      def get(self, students_id):
          if students_id not in STUDENTS:
            return "Not found", 404
          else:
            return STUDENTS[students_id]


      def put(self, students_id):
          parser.add_argument("firstname")
          parser.add_argument("lastname")
          args = parser.parse_args()
          if students_id not in STUDENTS:
              return "Record not found", 404
          else:
             student = STUDENTS[students_id]
             student["firstname"] = args["firstname"] if args["firstname"] is not None else student["firstname"]
             student["lastname"] = args["lastname"] if args["lastname"] is not None else student["lastname"]
             return student, 200

      def delete(self, students_id):
          if students_id not in STUDENTS:
           return "Not found", 404
          else:
             del STUDENTS[students_id]
             return '', 204


api.add_resource(StudentsList, '/Students')
api.add_resource(Student, '/Students/<students_id>')


if __name__ == '__main__':
    app.run(debug=True, port=80, host="0.0.0.0")

