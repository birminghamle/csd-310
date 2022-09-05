""" 
    Title: pytech_queries.py
    Author: Lathan Birmingham
    Date: 5 September 2022
    Description: Test program for querying the students collection.
"""

""" import statements """
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:<password>@cluster0.hccdu34.mongodb.net/test"

# connect to the MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

# get the students collection 
students = db.students

# find all students in the collection 
student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# find document by student_id
lathan = students.find_one({"student_id": "1007"})
bob = students.find_one({"student_id": "1008"})
alice = students.find_one({"student_id": "1009"})

# output the results 
print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + lathan["student_id"] + "\n  First Name: " + lathan["first_name"] + "\n  Last Name: " + lathan["last_name"] + "\n")
print("  Student ID: " + bob["student_id"] + "\n  First Name: " + bob["first_name"] + "\n  Last Name: " + bob["last_name"] + "\n")
print("  Student ID: " + alice["student_id"] + "\n  First Name: " + alice["first_name"] + "\n  Last Name: " + alice["last_name"] + "\n")



# exit message 
input("\n\n  End of program, press any key to continue...")
