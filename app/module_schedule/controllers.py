from flask import Flask, Blueprint, jsonify, abort, request, current_app, session, json, request
import logging


app = Flask(__name__)
mod_schedule = Blueprint('schedule', __name__)

if __name__ == '__main__':
    app.run(debug=True)

#get the db object to query
from app import db
from app.module_schedule.models import Lecture, Semester, Tutorial, Lab, AcademicRecord, Mapping, Course, Student

@mod_schedule.route('/add_lecture', methods=['POST'])
def add_lecture():
    student = get_student()
    info = request.form['lecture_id']
    info_split = info.split('/')
    lecture_code = info_split[0]
    lecture_section = info_split[1]

    course = db.session.query(Course).filter_by(full_name=lecture_code).first()
    lecture = db.session.query(Lecture).filter_by(course_id=course.id, section=lecture_section).first()
    return student.register_lecture(lecture.id)

@mod_schedule.route('/delete_lecture', methods=['GET', 'POST'])
def delete_lecture():
    student = get_student()
    info = request.form['lecture_id']
    info_split = info.split('/')
    lecture_code = info_split[0]
    lecture_section = info_split[1]

    course = db.session.query(Course).filter_by(full_name=lecture_code).first()
    lecture = db.session.query(Lecture).filter_by(course_id=course.id, section=lecture_section).first()

    if student.delete_lecture(lecture.id):
        return 'lecture successfully deleted'
    else:
        return 'lecture not deleted'

def get_student():
    return db.session.query(Student).filter_by(full_name=session['user_id']).first()

def get_course(course_id):
    return db.session.query(Course).filter_by(id=course_id).first()

def get_lecture(lecture_id):
    return db.session.query(Lecture).filter_by(id=lecture_id).first()


@mod_schedule.route('/complete_course', methods=['GET', 'POST'])
def complete_course():
	info = request.form['course_id']
	info_split = info.split('/')
	program = info_split[0]
	number = info_split[1]

	course = db.session.query(Course).filter_by(program=program, number=number).first()
	lecture = db.session.query(Lecture).filter_by(course_id=course.id).first()

	ac = db.session.query(AcademicRecord).filter_by(user_id=session['user_id'], lecture_id=lecture.id, lecture_status='registered').first()
	db.session.add(AcademicRecord(session['user_id'], lecture.id, 'completed'))
	db.session.delete(ac)
	db.session.commit()

	return True


#Gets all the lectures for a specified semester (id from 1-4)
@mod_schedule.route('/lectures_semester', methods=['POST'])
def get_lectures(semester_integer):
    lectures = db.session.query(Lecture).filter_by(semester_id=semester_integer).all()

    if(current_app):
        return jsonify(lectures=lectures)


@mod_schedule.route('/get_prerequisites', methods=['GET', 'POST'])
def get_prerequisites():
    info = request.form['lecture_id']
    info_split = info.split('/')
    lecture_code = info_split[0]

    course = db.session.query(Course).filter_by(full_name=lecture_code).first()

    mappings = db.session.query(Mapping).filter_by(course_id=course.id).all()
    prerequisites = []
    for mapping in mappings:
        prerequisites.append(db.session.query(Course).filter_by(id=mapping.course_req_id).first())

    return jsonify(courses=[course.serialize() for course in prerequisites])


@mod_schedule.route('/student_completed_courses', methods=['GET', 'POST'])
def get_student_completed_courses():
	student = get_student()
	completed_courses = student.get_completed_courses()

	return jsonify(courses=[course.serialize() for course in completed_courses])

@mod_schedule.route('/student_registered_courses', methods=['GET', 'POST'])
def get_student_registered_courses():
	student = get_student()
	registered_courses = student.get_registered_courses()

	return jsonify(courses=[course.serialize() for course in registered_courses])

@mod_schedule.route('/student_future_courses', methods=['GET', 'POST'])
def get_student_future_courses():
	return None #TO DO


@mod_schedule.route('/student_fall_lectures', methods=['GET'])
def student_fall_lectures():
	student = get_student()
	fall_lectures = student.get_fall_lectures()

	return jsonify(lectures=[lecture.serialize() for lecture in fall_lectures])


@mod_schedule.route('/student_winter_lectures', methods=['GET'])
def student_winter_lectures():
	student = get_student()
	winter_lectures = student.get_winter_lectures()

	return jsonify(lectures=[lecture.serialize() for lecture in winter_lectures])


@mod_schedule.route('/student_summer_lectures', methods=['GET'])
def student_summer_lectures():
	student = get_student()
	summer_lectures = student.get_summer_lectures()

	return jsonify(lectures=[lecture.serialize() for lecture in summer_lectures])


@mod_schedule.route('/fall_lectures', methods=['GET'])
def get_fall_lectures():
	lectures = []
	semesters = db.session.query(Semester).filter_by(semester_id=0).all()
	for semester in semesters:
	    lecture = db.session.query(Lecture).filter_by(id=semester.lecture_id).first()
	    if lecture is not None and lecture.get_course() is not None:
	        lectures.append(lecture)

	return jsonify(lectures=[lecture.serialize() for lecture in lectures])

@mod_schedule.route('/fall_lectures_search', methods=['GET', 'POST'])
def get_fall_lectures_search():
	lectures = []
	search = request.form['search']
	semesters = db.session.query(Semester).filter_by(semester_id=0).all()
	for semester in semesters:
		lecture = db.session.query(Lecture).filter_by(id=semester.lecture_id).first()
		if lecture is not None and lecture.get_course() is not None:
			if search.upper() in lecture.get_course().full_name:
				lectures.append(lecture)

	return jsonify(lectures=[lecture.serialize() for lecture in lectures])


@mod_schedule.route('/winter_lectures', methods=['GET'])
def get_winter_lectures():
	lectures = []
	semesters = db.session.query(Semester).filter_by(semester_id=1).all()
	for semester in semesters:
	    lecture = db.session.query(Lecture).filter_by(id=semester.lecture_id).first()
	    if lecture is not None and lecture.get_course() is not None:
	        lectures.append(lecture)

	return jsonify(lectures=[lecture.serialize() for lecture in lectures])


@mod_schedule.route('/winter_lectures_search', methods=['GET', 'POST'])
def get_winter_lectures_search():
	lectures = []
	search = request.form['search']
	semesters = db.session.query(Semester).filter_by(semester_id=1).all()
	for semester in semesters:
		lecture = db.session.query(Lecture).filter_by(id=semester.lecture_id).first()
		if lecture is not None and lecture.get_course() is not None:
			if search.upper() in lecture.get_course().full_name:
				lectures.append(lecture)

	return jsonify(lectures=[lecture.serialize() for lecture in lectures])


@mod_schedule.route('/summer_lectures', methods=['GET'])
def get_summer_lectures():
	lectures = []
	semesters = db.session.query(Semester).filter_by(semester_id=2).all()
	for semester in semesters:
	    lecture = db.session.query(Lecture).filter_by(id=semester.lecture_id).first()
	    if lecture is not None and lecture.get_course() is not None:
	        lectures.append(lecture)

	return jsonify(lectures=[lecture.serialize() for lecture in lectures])

@mod_schedule.route('/summer_lectures_search', methods=['GET', 'POST'])
def get_summer_lectures_search():
	lectures = []
	search = request.form['search']
	semesters = db.session.query(Semester).filter_by(semester_id=2).all()
	for semester in semesters:
		lecture = db.session.query(Lecture).filter_by(id=semester.lecture_id).first()
		if lecture is not None and lecture.get_course() is not None:
			if search.upper() in lecture.get_course().full_name:
				lectures.append(lecture)

	return jsonify(lectures=[lecture.serialize() for lecture in lectures])

# Gets the lab for a specified lecture
@mod_schedule.route('/labs', methods=['GET','POST'])
def get_labs(lecture_id):
    labs = db.session.query(Lab).filter_by(lecture_id=lecture_id).all()
    if(current_app):
        return jsonify(labs=labs)


# Gets the lectures a student is registered for
@mod_schedule.route('/student_lectures', methods=['GET'])
def get_student_lectures():
    student = get_student()
    return jsonify(lectures=student.get_lectures())


# Gets the lectures a student is registered for
@mod_schedule.route('/register', methods=['POST'])
def register_lecture(lecture_id):
    student = get_student()
    return student.register_lecture(lecture_id)


# Gets the lectures a student is registered for
@mod_schedule.route('/completed_course', methods=['GET', 'POST'])
def student_completed_course(course_id):
    student = get_student()
    return student.completed_course(course_id)

if __name__ == '__main__':
    app.run(debug=True)
