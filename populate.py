import csv
import re

from app import db
from app.module_schedule.models import Course, Lecture, Lab, Tutorial, Sequence, Mapping, Elective, AcademicRecord, Semester

def getDays(days):
    return re.split(r'[-]+', days)


def getSemesterId(sem):
    return {
        'Fall': 0,
        'Winter': 1,
        'Summer': 2
    }.get(sem, -1)


def parseCourses():
    with open("app/db_init/data/courses.csv") as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            print row
            db.session.add(Course(row['program'], row['credits'], row['number'], row['name ']))
            db.session.commit()


parseCourses()

def parseLectures():
    with open("app/db_init/data/lectures.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            days = getDays(row['days'])
            semester_id = getSemesterId(row['semester'])
            print semester_id
            db.session.add(Lecture(row['instructor'], row['course_id'], semester_id, row['start_time'], row['end_time'], days[0], days[1]))
            db.session.add(Semester(semester_id, row['course_id']))
            db.session.commit()

parseLectures()

def parseLabs():
    with open("app/db_init/data/labs.csv") as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            days = getDays(row['days'])
            print row['lecture_id']
            db.session.add(Lab(row['lecture_id'], row['section_code'], row['start_time'], row['end_time'], days[0]))
            db.session.commit()

parseLabs()

def parseTutorials():
    with open("app/db_init/data/tutorials.csv") as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            days = getDays(row['days'])
            print row['lecture_id']
            db.session.add(Tutorial(row['lecture_id'], row['section_code'], row['start_time'], row['end_time'], days[0], days[1]))
            db.session.commit()


parseTutorials()

def parseSequences():
    files = ['sequenceAvionics.csv', 'sequenceGames.csv', 'sequenceGeneral.csv', 'sequenceWeb.csv']
    options = ['Avionics', 'Games', 'General', 'Web']
    index = -1
    for file in files:
        index = index + 1
        opt = options[index]
        with open('app/db_init/data/SequenceRequired/'+file) as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                print opt + '  ' + row['course_id']
                db.session.add(Sequence(opt, row['course_id']))
                db.session.commit()

parseSequences()

def parsePrerequisites():
    with open('app/db_init/data/course_prereqs.csv') as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            print row['id'] + '  ' + row['course_id']
            db.session.add(Mapping(row['course_id'], row['prereq_type_id'], row['course_id_prereq']))
            db.session.commit()


parsePrerequisites()

def parseTechElectives():
    files = ['AvionicsOptElectives.csv', 'GamesOptElectives.csv', 'GeneralOptElectives.csv', 'WebOptElectives.csv']
    options = ['Avionics', 'Games', 'General', 'Web']
    index = -1
    for file in files:
        index = index + 1
        with open('app/db_init/data/SequenceElectives/'+file) as csvFile:
            reader = csv.DictReader(csvFile)
            opt = options[index]
            print opt
            for row in reader:
                db.session.add(Elective(opt, row['course_id']))
                db.session.commit()
                

parseTechElectives()

def parseOtherElectives():
    files = ['BasicScienceElectives.csv', 'GeneralElectives.csv']
    options = ['Basic_science', 'General_elective']
    index = -1
    for file in files:
        index = index + 1
        with open('app/db_init/data/'+file) as csvFile:
            reader = csv.DictReader(csvFile)
            opt = options[index]
            print opt
            for row in reader:
                db.session.add(Elective(opt, row['course_id']))
 

parseOtherElectives()

