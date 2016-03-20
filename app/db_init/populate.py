import csv
import re


def parseCourses():
    with open("data/course.csv") as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            # db.session.add(Course(row['program'], row['credits'], row['number'], row['name']))
            # db.session.commit()


# def parseLectures():
#     with open("data/lectures.csv") as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             days = getDays(row['days'])
#             semester_id = getSemesterId(row['semester'])
#             print semester_id
#             #db.session.add(Lecture(row['instructor'], row['course_id'], semester_id))
#             #db.session.commit()


def parseLabs():
    with open("data/labs.csv") as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            days = getDays(row['days'])
            db.session.add(Lecture(row['code'], row['start_time'], row['end_time'], row['end_time'], days))


def parseTutorials():
    with open("data/tutorials.csv") as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            days = getDays(row['days'])
            db.session.add(Lecture(row['lecture_id'], row['section_code'], row['day'], row['end_time'], days))


def parseSequences():
    files = ['sequenceAvionics.csv', 'sequenceGames.csv', 'sequenceGeneral.csv', 'sequenceWeb.csv']
    for file in files:
        with open('data/SequenceRequired'+file) as csv_file:
            reader = csv.DictReader(csv_file)
            opt = file[8, file.index('.')]
            sequences.insert().values(option=opt, course_id=row['course_id'])


def parseSequences():
    # Fix paths - this won't work
    files = ['sequenceAvionics.csv', 'sequenceGames.csv', 'sequenceGeneral.csv', 'sequenceWeb.csv']
    for file in files:
        with open(file) as csv_file:
            reader = csv.DictReader(csv_file)
            opt = file[8, file.index('.')]
            sequences.insert().values(option=opt, course_id=row['course_id'])


def getDays(days):
    return filter(None, re.split(r'[-]+', days))


def getSemesterId(sem):
    return {
        'Fall': 0,
        'Winter': 1,
        'Summer': 2
    }.get(sem, -1)

parseSequences()
