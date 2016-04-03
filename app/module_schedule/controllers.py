from flask import Flask, Blueprint, jsonify, abort, request, current_app, session, json

app = Flask(__name__)
mod_schedule = Blueprint('schedule', __name__)

# Test Data - to be removed later
# JSON stores values in key-value pairs
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
from app.module_schedule.models import Lecture, Semester, Tutorial, Lab, AcademicRecord, Mapping, Course, Student

def get_student():
    return db.session.query(Student).filter_by(full_name=session['user_id']).first()

def get_course(course_id):
    return db.session.query(Course).filter_by(id=course_id).first()

def get_lecture(lecture_id):
    return db.session.query(Lecture).filter_by(id=lecture_id).first()

#Gets all the lectures for a specified semester (id from 1-4)
@mod_schedule.route('/lectures_semester', methods=['POST'])
def get_lectures(semester_integer):
    lectures = db.session.query(Lecture).filter_by(semester_id=semester_integer).all()

    if(current_app):
        return jsonify(lectures=lectures)


#Gets all the lectures of a specified course id
@mod_schedule.route('/lectures_course', methods=['GET','POST'])
def get_lectures_for_course(course_number):
    lectures = db.session.query(Lecture).filter_by(course_id=course_number).all()
    if(current_app):
        return jsonify(lectures=lectures)


# Gets the tutorial for a specified lecture
@mod_schedule.route('/tutorials', methods=['GET','POST'])
def get_tutorials(lecture_id):
    tutorials = db.session.query(Tutorial).filter_by(lecture_id=lecture_id).all()
    if(current_app):
        return jsonify(tutorials=tutorials)



# Gets the tutorial for a specified lecture
@mod_schedule.route('/test', methods=['GET','POST'])
def test():
    lecture = db.session.query(Lecture).filter_by(id=1).first()
    name = lecture.get_course().name
    print name

    return jsonify(name=name)




@mod_schedule.route('/fall_lectures', methods=['GET'])
def get_fall_lectures():
    semesters = db.session.query(Semester).filter_by(semester_id=0).all()
    lectures = []
    for semester in semesters:
        lecture = db.session.query(Lecture).filter_by(id=semester.lecture_id).first()
        if lecture is not None:
            lectures.append(lecture)

    return jsonify(lectures=[lecture.serialize() for lecture in lectures])


@mod_schedule.route('/winter_lectures', methods=['GET', 'POST'])
def get_winter_courses():
    semesters = db.session.query(Semester).filter_by(semester_id=1).all()
    lectures = []
    for semester in semesters:
        lecture = db.session.query(Lecture).filter_by(id=semester.lecture_id).first()
        if lecture is not None:
            lectures.append(lecture)

    #return jsonify(lectures=[lecture.serialize() for lecture in lectures])


@mod_schedule.route('/summer_lectures', methods=['GET', 'POST'])
def get_summer_courses():
    semesters = db.session.query(Semester).filter_by(semester_id=2).all()

    lectures = []
    for semester in semesters:
        lecture = db.session.query(Lecture).filter_by(id=semester.lecture_id).first()
        if lecture is not None:
            lectures.append(lecture)

    return jsonify(lectures=[lecture.serialize() for lecture in lectures])

# Gets the lab for a specified lecture
@mod_schedule.route('/labs', methods=['GET','POST'])
def get_labs(lecture_id):
    labs = db.session.query(Lab).filter_by(lecture_id=lecture_id).all()
    if(current_app):
        return jsonify(labs=labs)


# Gets the lectures a student is registered for
@mod_schedule.route('/student_lectures', methods=['GET','POST'])
def get_student_lectures():
    student = get_student()
    return jsonify(lectures=student.get_lectures())


# Gets the lectures a student is registered for
@mod_schedule.route('/register', methods=['GET','POST'])
def register_lecture(lecture_id):
    student = get_student()
    return student.register_lecture(lecture_id)


# Gets the lectures a student is registered for
@mod_schedule.route('/completed_course', methods=['GET','POST'])
def student_completed_course(course_id):
    student = get_student()
    return student.completed_course(course_id)


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
