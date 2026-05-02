import json
with open('student.json', 'r') as file:
          students = json.load(file)
    
def print_students(students_list):
    for student in students_list:
        print(student["L_Name"] + ", " + student["F_Name"] +
              " : ID = " + str(student["Student_ID"]) + 
              " , Email = " + student["Email"])

print("Original Students List")
print_students(students)

students.append({
    "F_Name": "Jordyn",
    "L_Name": "Rylander",
    "Student_ID": 542544,
    "Email": "jordynrylander@gmail.com"
})
print("\nUpdated Students List")
print_students(students)

with open("student.json", "w") as file:
    json.dump(students, file)

print("\nNew student added and saved to students.json")