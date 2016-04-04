import csv
import re

from app import db
from app.module_schedule.models import Student, Course, Lecture, Lab, Tutorial, Sequence, Mapping, Elective, AcademicRecord, Semester
from app.module_authentication.models import User

def getDays(days):
    return re.split(r'[-]+', days)


def getSemesterId(sem):
    return {
        'Fall': 0,
        'Winter': 1,
        'Summer': 2
    }.get(sem, -1)


def parseCourses():
    print "Parsing software engineering courses..."
    with open("app/db_init/data/courses.csv") as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            db.session.add(Course(row['program'], row['credits'], row['number'], row['name ']))
            db.session.commit()
    print "Parsing successful"


def parseLectures():
    print "Parsing software engineering course lectures..."
    with open("app/db_init/data/lectures.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        number = 1
        for row in reader:
            days = getDays(row['days'])
            semester_id = getSemesterId(row['semester'])
            db.session.add(Lecture(row['instructor'], row['course_id'], row['section_code'], semester_id, row['start_time'], row['end_time'], days[0], days[1]))
            db.session.add(Semester(semester_id, number))
            number = number + 1
            db.session.commit()

    print "Parsing successful"


def parseLabs():
    print "Parsing software engineering course labs..."
    with open("app/db_init/data/labs.csv") as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            days = getDays(row['days'])
            db.session.add(Lab(row['lecture_id'], row['section_code'], row['start_time'], row['end_time'], days[0]))
            db.session.commit()
    print "Parsing successful"


def parseTutorials():
    print "Parsing software engineering course tutorials..."
    with open("app/db_init/data/tutorials.csv") as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            days = getDays(row['days'])
            db.session.add(Tutorial(row['lecture_id'], row['section_code'], row['start_time'], row['end_time'], days[0], days[1]))
            db.session.commit()
    print "Parsing successful"


def parseSequences():
    print "Parsing software engineering course sequences..."
    files = ['sequenceAvionics.csv', 'sequenceGames.csv', 'sequenceGeneral.csv', 'sequenceWeb.csv']
    options = ['Avionics', 'Games', 'General', 'Web']
    index = -1
    for file in files:
        index = index + 1
        opt = options[index]
        with open('app/db_init/data/SequenceRequired/'+file) as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                db.session.add(Sequence(opt, row['course_id']))
                db.session.commit()


def parsePrerequisites():
    print "Parsing course prerequisites..."
    with open('app/db_init/data/course_prereqs.csv') as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            db.session.add(Mapping(row['course_id'], row['prereq_type_id'], row['course_id_prereq']))
            db.session.commit()


def parseTechElectives():
    print "Parsing software engineering electives..."
    files = ['AvionicsOptElectives.csv', 'GamesOptElectives.csv', 'GeneralOptElectives.csv', 'WebOptElectives.csv']
    options = ['Avionics', 'Games', 'General', 'Web']
    index = -1
    for file in files:
        index = index + 1
        with open('app/db_init/data/SequenceElectives/'+file) as csvFile:
            reader = csv.DictReader(csvFile)
            opt = options[index]
            for row in reader:
                db.session.add(Elective(opt, row['course_id']))
                db.session.add(Sequence(opt, row['course_id']))
                db.session.commit()


def parseOtherElectives():
    print "Parsing non software engineering electives..."
    files = ['BasicScienceElectives.csv', 'GeneralElectives.csv']
    options = ['Basic_science', 'General_elective']
    index = -1
    for file in files:
        index = index + 1
        with open('app/db_init/data/'+file) as csvFile:
            reader = csv.DictReader(csvFile)
            opt = options[index]
            for row in reader:
                db.session.add(Elective(opt, row['course_id']))
                db.session.add(Sequence(opt, row['course_id']))
                db.session.commit()
 

def createUsers():
    print 'creating users...'
    robert_user = User('robert', 'robert', 'email@email.com')
    robert_student = Student('robert', None, None, robert_user.id)
    db.session.add(robert_student)
    db.session.add(robert_user)

    josh_user = User('joshua', 'joshua', 'email@email.com')
    josh_student = Student('joshua', None, None, josh_user.id)
    db.session.add(josh_student)
    db.session.add(josh_user)

    david_user = User('david', 'david', 'email@email.com')
    david_student = Student('david', None, None, david_user.id)
    db.session.add(david_student)
    db.session.add(david_user)

    darrel_user = User('darrel', 'darrel', 'email@email.com')
    darrel_student = Student('darrel', None, None, darrel_user.id)
    db.session.add(darrel_student)
    db.session.add(darrel_user)

    ioan_user = User('ioan', 'ioan', 'email@email.com')
    ioan_student = Student('ioan', None, None, ioan_user.id)
    db.session.add(ioan_student)
    db.session.add(ioan_user)

    harrison_user = User('harrison', 'harrison', 'email@email.com')
    harrison_student = Student('harrison', None, None, harrison_user.id)
    db.session.add(harrison_student)
    db.session.add(harrison_user)

    simeon_user = User('simeon', 'simeon', 'email@email.com')
    simeon_student = Student('simeon', None, None, simeon_user.id)
    db.session.add(simeon_student)
    db.session.add(simeon_user)

    george_user = User('george', 'george', 'email@email.com')
    george_student = Student('george', None, None, george_user.id)
    db.session.add(george_student)
    db.session.add(george_user)

    ali_user = User('ali', 'ali', 'email@email.com')
    ali_student = Student('ali', None, None, ali_user.id)
    db.session.add(ali_student)
    db.session.add(ali_user)

    philippe_user = User('philippe', 'philippe', 'email@email.com')
    philippe_student = Student('philippe', None, None, philippe_user.id)
    db.session.add(philippe_student)
    db.session.add(philippe_user)

    db.session.commit()

    print 'done creating users.'

def populate():
    parseCourses()
    parseLectures()
    parseLabs()
    parseTutorials()
    parseSequences()
    parsePrerequisites()
    parseTechElectives()
    parseOtherElectives()
    createUsers()
