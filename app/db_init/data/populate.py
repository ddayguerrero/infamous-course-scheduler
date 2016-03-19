import csv
from app import db

# Do not start populating, proper model structure required
def parseLecture():
    with open("lectures.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if (row['semester'] == 'Fall'):
                print(row['instructor'])
            elif (row['semester'] == 'Winter'):
                print(row['instructor'])
            elif (row['semester'] == 'Summer'):
                print(row['instructor'])
