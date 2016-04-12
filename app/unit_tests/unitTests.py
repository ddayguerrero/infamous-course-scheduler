import unittest
import app
from app import db
from flask import session, sqlalchemy
from app.module_schedule import models
from app.module_schedule.models import Student, Course, Lecture, Lab, Tutorial, Mapping, Sequence, Semester
from app.module_schedule.controllers import register, time_conflict, login, logout, student_lectures, add_lecture, delete_lecture, preview_lectures  
from app.module_schedule.controllers import student_fall_lectures, student_winter_lectures, student_summer_lectures


class TestClass(unittest.TestCase):

	def test_register(self, username, password):
		self.assertTrue(register(username, password))
		self.assertFalse(register('bad_username', password))
		self.assertFalse(register(username, 'bad_password'))
		self.assertFalse(register('bad_username', 'bad_password'))


	def test_login(self, username, password):
		self.assertTrue(login(username, password))
		self.assertFalse(login('bad_username', password))
		self.assertFalse(login(username, 'bad_password'))
		self.assertFalse(login('bad_username', 'bad_password'))


	def test_logout(self):
		session = session['user_id']

		self.assertTrue(logout(session))
		self.assertFalse(logout(None))


	def test_student_lectures(self, test_lecture):
		student = db.session.query(Student).filter_by(id=session['user_id']).first()

		assertTrue(student_lectures(student, 'COMP232'))
		assertFalse(student_lectures(student, test_lecture))


	def register_course(self, course_id):
		student = db.session.query(Student).filter_by(id=session['user_id']).first()
		course = db.session.query(Course).filter_by(id=course_id).first()
		course_bad = db.session.query(Course).filter_by(id=-2).first()

		assertTrue(register_course(student, course))
		assertFalse(register_course(student,course_bad))


	def delete_course(self, course_id):
		student = db.session.query(Student).filter_by(id=session['user_id']).first()
		course = db.session.query(Course).filter_by(id=course_id).first()
		course_bad = db.session.query(Course).filter_by(id=-2).first()

		assertTrue(delete_course(student, course))
		assertFalse(delete_course(student,course_bad))


	def test_student_fall_lectures(self, test_lecture):
		student = db.session.query(Student).filter_by(id=session['user_id']).first()

		assertTrue(student_fall_lectures(student, 'COMP232'))
		assertFalse(student_fall_lectures(student, test_lecture))


	def test_student_winter_lectures(self, test_lecture):
		student = db.session.query(Student).filter_by(id=session['user_id']).first()

		assertTrue(student_winter_lectures(student, 'COMP232'))
		assertFalse(student_winter_lectures(student, test_lecture))


	def test_student_summer_lectures(self, test_lecture):
		student = db.session.query(Student).filter_by(id=session['user_id']).first()

		assertTrue(student_summer_lectures(student, 'COMP232'))
		assertFalse(student_summer_lectures(student, test_lecture))
