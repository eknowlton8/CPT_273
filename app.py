# Flask Library
from flask import Flask, jsonify, request


# Create App Object
app = Flask(__name__)


# List of Students
students = [
    {
        "id": 1,
        "name": 'tom'
    },
    {
        "id": 2,
        "name": "Jerry"
    },
    {
        "id": 3,
        "name": "Bugs Bunny"
    }
]

#### ASSIGNMENT STARTS HERE ####
@app.route('/', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/<int:id>', methods=['GET'])
def get_id(id):
    student = next((s for s in students if s['id'] == id), None)
    if student:
        return jsonify(student)
    return jsonify({'error': 'ID not found'}), 404

@app.route('/', methods=['POST'])
def add_student():
    new_student = request.get_json()
    students.append(new_student)
    return jsonify(new_student), 201

@app.route('/<int:id>', methods=['PUT'])
def update_name(id):
    student = next((s for s in students if s['id'] == id), None)
    if student:
        data = request.get_json()
        student['name'] = data['name']
        return jsonify(student)
    return jsonify({'error': 'Name not found'}), 404

@app.route('/<int:id>', methods=['DELETE'])
def delete_student(id):
    global students
    students = [s for s in students if s['id'] != id]
    return jsonify({'message': 'Student deleted'}), 200

#### ASSIGNMENT ENDS HERE ####

if __name__ == '__main__':
    app.run(debug=True)
