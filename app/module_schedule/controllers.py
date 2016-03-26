from flask import Flask, Blueprint, jsonify, abort, request

from app.module_authentication.forms import CourseSelection


app = Flask(__name__)
mod_schedule = Blueprint('schedule', __name__)

# Test Data - to be removed later
# JSON stores values in key-value pairs
courses = [
    {
        'id': 1,
        'program': 'ENGR',
        'number': 201,
        'credits': 1.5,
        'name': "Professional Practice and Responsibility"
    },
    {
        'id': 2,
        'program': 'ENGR',
        'number': 202,
        'credits': 3,
        'name': 'Sustainable Development and Environmental Stewardship'
    }
]

schedules = [
    {
        'id': 1,
        'name': "Lerrad"
    },
    {
        'id': 2,
        'name': "Neomis"
    },
    {
        'id': 3,
        'name': "Divad"
    }
]

lectures = [
    {
        'instructor': 'Don Davis',
        'id': '1',
        'semester_id': '1',
        'tutorials': [
            {'id': '2', 'startTime': '8:00','endTime': '9:00','dayOne': 'Monday', 'dayOne': 'Wednesday'},
            {'id': '2','startTime': '11:00','endTime': '12:00','dayOne': 'Monday', 'dayTwo': 'Wednesday'},
            {'id': '3', 'startTime': '8:00','endTime': '9:00','dayOne': 'Monday', 'dayOne': 'Wednesday'},
            {'id': '3','startTime': '11:00','endTime': '12:00','dayOne': 'Monday', 'dayTwo': 'Wednesday'}
        ],
        'labs': [
             {'id': '4', 'startTime': '10:00','endTime': '11:00','dayOne': 'Monday', 'dayOne': 'Wednesday'},
             {'id': 'None', 'startTime': 'None','endTime': 'None','dayOne': 'None', 'dayTwo': 'None'}
        ],
        'startTime': '18:00',
        'endTime': '21:00',
        'dayOne': 'Monday',
        'dayTwo': 'None'
    }
]



# RESTful resources must be defined as 'nouns' not verbs
# e.g. /courses istead of /addcourses
#
# GET request example
@mod_schedule.route('/courses', methods=['GET'])
def get_courses():
    # logic goes here
    return jsonify({'courses': courses})

if __name__ == '__main__':
    app.run(debug=True)


# Say you want to retrieve a specific course (e.g. based on id)
#
# GET request example
@mod_schedule.route('/courses/<int:id>', methods=['GET'])
def get_course(id):
    course = [course for course in courses if course['id'] == id]

    # no existing course
    if len(course) == 0:
        abort(404)

    return jsonify({'course': course[0]})

if __name__ == '__main__':
    app.run(debug=True)


# Say you want to create a specific resource (e.g. schedule)
#
# POST request example
@mod_schedule.route('/schedules', methods=['POST'])
def generate_schedule():
    if not request.json or 'name' not in request.json:
        abort(400)
    schedule = {
        'id': schedules[-1]['id'] + 1,  # schedule is equal to last schedule id + 1
        'name': request.json['name'],
        'done': False
    }
    schedules.append(schedule)
    return jsonify({'schedule': schedule}), 201


@mod_schedule.route('/changeCalendar', methods=['GET', 'POST'])
def verifyCourse():
    form = CourseSelection()
    # addCourse(form.courseName.data) implement 
    return None