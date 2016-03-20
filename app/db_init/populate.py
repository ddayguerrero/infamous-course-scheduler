import csv
import re


def parseLectures():
    # Fix paths - this won't work
    with open("data/lectures.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            days = filter(None, re.split(r'[-]+', row['days']))
            semester_id = getSemesterId(row['semester'])
            print semester_id
            # db.session.add(Lecture(row['instructor'], row['course_id'], semester_id))

def getSemesterId(sem):
    return {
        'Fall': 0,
        'Winter': 1,
        'Summer': 2
    }.get(sem, -1)
            

parseLectures()
