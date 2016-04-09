from flask import Flask, Blueprint, jsonify, abort, request, current_app, session, json, request
import logging


app = Flask(__name__)
mod_schedule = Blueprint('schedule', __name__)

if __name__ == '__main__':
    app.run(debug=True)

#get the db object to query
from app import db
from app.module_schedule.models import Lecture, Semester, Tutorial, Lab, AcademicRecord, Mapping, Course, Student, Sequence

@mod_schedule.route('/web_sequence_courses', methods=['GET', 'POST'])
def get_web_courses():
    sequences = db.session.query(Sequence).filter_by(option='Web').all()
    courses = []
    for sequence in sequences:
        courses.append(db.session.query(Course).filter_by(id=sequence.course_id).first())

    return jsonify(courses=[course.serialize() for course in courses])

@mod_schedule.route('/avionics_sequence_courses', methods=['GET', 'POST'])
def get_avionics_courses():
    sequences = db.session.query(Sequence).filter_by(option='Avionics').all()
    courses = []
    for sequence in sequences:
        courses.append(db.session.query(Course).filter_by(id=sequence.course_id).first())

    return jsonify(courses=[course.serialize() for course in courses])

@mod_schedule.route('/general_sequence_courses', methods=['GET', 'POST'])
def get_general_courses():
    sequences = db.session.query(Sequence).filter_by(option='General').all()
    courses = []
    for sequence in sequences:
        courses.append(db.session.query(Course).filter_by(id=sequence.course_id).first())

    return jsonify(courses=[course.serialize() for course in courses])

@mod_schedule.route('/games_sequence_courses', methods=['GET', 'POST'])
def get_games_courses():
    sequences = db.session.query(Sequence).filter_by(option='Games').all()
    courses = []
    for sequence in sequences:
        courses.append(db.session.query(Course).filter_by(id=sequence.course_id).first())

    return jsonify(courses=[course.serialize() for course in courses])


@mod_schedule.route('/complete_course', methods=['GET', 'POST'])
def complete_course():
    info = request.form['course_id']
    info_split = info.split('/')
    program = info_split[0]
    number = info_split[1]

    course = db.session.query(Course).filter_by(program=program, number=number).first()

    ac = db.session.query(AcademicRecord).filter_by(user_id=session['user_id'], course_id=course.id, lecture_status='registered').first()
    if ac is not None:
        db.session.add(AcademicRecord(session['user_id'], -1, course.id, 'completed'))
        db.session.delete(ac)
        db.session.commit()
        return True
    else:
        return False

@mod_schedule.route('/uncomplete_course', methods=['GET', 'POST'])
def uncomplete_course():
    info = request.form['course_id']
    info_split = info.split('/')
    program = info_split[0]
    number = info_split[1]

    course = db.session.query(Course).filter_by(program=program, number=number).first()
    ac = db.session.query(AcademicRecord).filter_by(user_id=session['user_id'], course_id=course.id, lecture_status='completed').first()
    if ac is not None:
        db.session.delete(ac)
        db.session.commit()
        return True
    else:
        return False

@mod_schedule.route('/add_lecture', methods=['POST'])
def add_lecture():
    student = get_student()
    info = request.form['lecture_id']
    info_split = info.split('/')
    lecture_code = info_split[0]
    lecture_section = info_split[1]

    course = db.session.query(Course).filter_by(full_name=lecture_code).first()
    lecture = db.session.query(Lecture).filter_by(course_id=course.id, section=lecture_section).first()
    return student.register_lecture(lecture.id, course.id)

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


@mod_schedule.route('/time_conflicts', methods=['GET', 'POST'])
def get_time_conflict(): 
    lecture_id1 = request.form['lecture_id1']
    lecture_id2 = request.form['lecture_id2']

    info1 = lecture_id1.split('/')
    info2 = lecture_id2.split('/')

    course1 = db.session.query(Course).filter_by(full_name=info1[0]).first()
    course2 = db.session.query(Course).filter_by(full_name=info2[0]).first()

    lecture1 = db.session.query(Lecture).filter_by(course_id=course1.id, section=info1[1]).first()
    lecture2 = db.session.query(Lecture).filter_by(course_id=course2.id, section=info2[1]).first()

    l1d1 = lecture1.day_one
    l2d1 = lecture2.day_one
    l1d2 = lecture1.day_two
    l2d2 = lecture2.day_two

    if l1d1 != "" and l2d1 != "":
        if l1d1 != l2d1 and l1d2 != l2d2:
            return "false"
        else:
            return is_time_conflict(lecture1.start_time, lecture1.end_time, lecture2.start_time, lecture2.end_time)

    elif l1d1 != "":
        if l1d1 != l2d1 and l1d1 != l2d2:
            return "false"
        else:
            return is_time_conflict(lecture1.start_time, lecture1.end_time, lecture2.start_time, lecture2.end_time)

    elif l2d1 != "":
        if l2d1 != l1d1 and l2d1 != l1d2:
            return "false"
        else:
            return is_time_conflict(lecture1.start_time, lecture1.end_time, lecture2.start_time, lecture2.end_time)

    else:
        if l1d2 != l2d2:
            return "false"
        else:
            return is_time_conflict(lecture1.start_time, lecture1.end_time, lecture2.start_time, lecture2.end_time)

def is_time_conflict(start1, end1, start2, end2):
    start_times1 = start1.split(':')
    start_times2 = start2.split(':')
    end_times1 = end1.split(':')
    end_times2 = end2.split(':')

    start1_str = start_times1[0] + start_times1[1]
    start1_int = int(start1_str)
    start2_str = start_times2[0] + start_times2[1]
    start2_int = int(start2_str)
    end1_str = end_times1[0] + end_times1[1]
    end1_int = int(end1_str)
    end2_str = end_times2[0] + end_times2[1]
    end2_int = int(end2_str)

    if (start1_int >= start2_int and start1_int <= end2_int) or (start2_int >= start1_int and start2_int <= end1_int):
        return "true"

    else:
        return "false"

if __name__ == '__main__':
    app.run(debug=True)
