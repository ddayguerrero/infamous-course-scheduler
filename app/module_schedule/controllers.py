from flask import Flask, Blueprint, jsonify, abort, request, current_app

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


if __name__ == '__main__':
    app.run(debug=True)

#get the db object to query
from app import db
from app.module_schedule.models import Lecture, Tutorial, Lab

#Gets all the lectures for a specified semester (id from 1-4)
@mod_schedule.route('/courses', methods=['GET','POST'])
def get_lectures(semester_integer):
    lectures = db.session.query(Lecture).filter_by(semester_id=semester_integer).all()
    if(current_app):
        return jsonify(lectures=lectures)


#Gets all the lectures of a specified course id
@mod_schedule.route('/courses', methods=['GET','POST'])
def get_lectures_for_course(course_number):
    lectures = db.session.query(Lecture).filter_by(course_id=course_number).all()
    if(current_app):
        return jsonify(lectures=lectures)


# Gets the tutorial for a specified lecture
@mod_schedule.route('/courses', methods=['GET','POST'])
def get_tutorials(lecture_id):
    tutorials = db.session.query(Tutorial).filter_by(lecture_id=lecture_id).all()
    if(current_app):
        return jsonify(tutorials=tutorials)


# Gets the lab for a specified lecture
@mod_schedule.route('/courses', methods=['GET','POST'])
def get_labs(lecture_id):
    labs = db.session.query(Lab).filter_by(lecture_id=lecture_id).all()
    if(current_app):
        return jsonify(labs=labs)


# Say you want to retrieve a specific course (e.g. based on id)
#
# GET request example
@mod_schedule.route('/courses', methods=['GET','POST'])
def get_course():
    course = request.form.get('course') #the course inputed by user to be added
    lecture = {
        'name':'ENGR 201',
        'instructor': 'Don Davis',
        'id': '1',
        'startTime': '18:00',
        'endTime': '21:00',
        'dayOne': 'Monday',
        'dayTwo': 'None'
    }
    return jsonify(lecture) #for now return the lecture object created at the top. this object has to be queried from database

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