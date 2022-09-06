""" 
    Title: pytech_insert.py
    Author: Lathan Birmingham
    Date: 4 September 2022
    Description: Test program for inserting new documents 
                 into the students collection 
"""

""" import statements """
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.hccdu34.mongodb.net/test"
# connect to the MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

""" three student documents"""
# lathan birmingham's data document 
lathan = {
    "student_id": "1007",
    "first_name": "Lathan",
    "last_name": "Birmingham",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "4.0",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor Krasso",
                    "grade": "A+"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Professor Krasso",
                    "grade": "A+"
                }
            ]
        }
    ]

}

# bob upsteam data document 
bob = {
    "student_id": "1008",
    "first_name": "Bob",
    "last_name": "Upsteam",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "3.4",
            "start_date": "July 10, 2022",
            "end_date": "September 14, 2022",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor Krasso",
                    "grade": "B+"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Professor Krasso",
                    "grade": "A-"
                }
            ]
        }
    ]
}

# alice data document
alice = {
    "student_id": "1009",
    "first_name": "Alice",
    "last_name": "Featherstone",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "3.2",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor Krasso",
                    "grade": "C"
                },
                {
                    "course_id": "CSD 320",
                    "description": "Programming with Java",
                    "instructor": "Professor Krasso",
                    "grade": "B"
                }
            ]
        }
    ]
}

# get the students collection 
students = db.students

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
lathan_student_id = students.insert_one(lathan).inserted_id
print("  Inserted student record Lathan Birmingham into the students collection with document_id " + str(lathan_student_id))

bob_student_id = students.insert_one(bob).inserted_id
print("  Inserted student record Bob Upsteam into the students collection with document_id " + str(bob_student_id))

alice_student_id = students.insert_one(alice).inserted_id
print("  Inserted student record Alice Featherstone into the students collection with document_id " + str(alice_student_id))

input("\n\n  End of program, press any key to exit... ")

