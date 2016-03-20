import csv
from app import db
import re
# Import the tables you need 
def parseAllFiles():
	# Call all helper functions
	parseCourseList()
	parseSequences()
	

def parseLectures():
	# Fix paths - this won't work
    with open("lectures.csv") as csvfile:
        reader = csv.DictReader(csvfile)
		for row in reader:
			days = filter(None,re.split(r'[-]+',row['days']))


# Combines these two into one function
def parseTutorials():
def parseLabs():

def parseCourseList():
	# Fix paths - this won't work
	with open('courses.csv') as csv_file:
		reader = csv.DictReader(csv_file)
		for row in reader:
			db.session.add(Course(row['program'], row['number'], row['credits'], row['name'])
		db.session.commit()
		
def parseSequences():
	# Fix paths - this won't work
	files = ['sequenceAvionics.csv', 'sequenceGames.csv', 'sequenceGeneral.csv', 'sequenceWeb.csv']
	for file in files:
		with open(file) as csv_file:
			reader = csv.DictReader(csv_file)
				# from the imported table, call insert().values(...)
				# ex: sequences.insert().values(option="Web")

def parsePrerequisites():
	# Fix paths - this won't work
	with open('course_prereqs.csv') as csv_file:
			reader = csv.DictReader(csv_file)

def parseElectives(files):
	
def parseSequenceElectives():
	#Sequences need a foreign key associated with sequence_electives table
