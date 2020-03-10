from teacher_class import *
from student_class import *
from monsters_class import *
from monster_workshops import *

# Creating a student
# student1 = Student('Maksaud', 'Ahmed', 1)
#
# list_of_student = []
#
# # A list of students
# list_of_student.append(student1)
#
# # Creating workshops
# workshop1 = MonsterWorkshop('Maths', 'mr man')
# workshop2 = MonsterWorkshop('English', 'mr woman')
#
# # Listing workshops
# list_of_workshop = []
#  # Putting each set of workshops into the list.
# list_of_workshop.append(workshop1.set_workshops()) # subject
# list_of_workshop.append(workshop2.set_workshops())
#
# print(list_of_workshop)
#
# # Creating a list of skills
# student1.skills.append('stealth')
# student1.skills.append('streangth')
#
#Printing all skiils of students
# print(student1.skills)

user_input = ""
database = {}
id = 0
while user_input != 'quit':
    user_input = input("If you want to add a student or teacher type: add, if you want to add a subject type: subject, if you want to add a skill: skill, if you want to quit: quit ")
    if user_input == 'add':
        student_or_teach = input('input a student or teacher ')
        if student_or_teach == 'student':
            database[id] = Student(input('Enter the students first name '), input('Enter students last name '), id)
            print(database[id].f_name, database[id].l_name + 'is added')
            id += 1
        elif student_or_teach == 'teacher':
            database[id] = Teacher(input('Enter the teachers first name '), input('Enter the teachers last name '), id)
            print(database[id].f_name, database[id].l_name + 'is added')
            id += 1
        else:
            user_input = 'quit'
    elif user_input == 'subject':
        workshop = MonsterWorkshops(input('Enter the subject name '), input('Enter teacher name '))
        database["workshops"] = {workshop.f_name:workshop.teacher}
    elif user_input == 'skill':
        skill_input = input('Enter a skill ')
        which_id = input("which id do you want to change ")
        which_id.skills.append(skill_input)
    else:
        user_input='quit'
