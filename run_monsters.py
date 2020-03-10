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
database = {'Workshops':{}}
id = 0

# Switch board
while user_input != 'quit':
    user_input = input("If you want to add a student or teacher type: add \n if you want to add a subject type: subject \n if you want to add a skill: skill \n if you want to print everything: print\n if you want to quit: quit \n")

    # adding either student or teacher
    if user_input == 'add':
        student_or_teach = input('input a student or teacher ')

        # creating a student object and added to dictinary
        if student_or_teach == 'student':
            database[str(id)] = Student(input('Enter the students first name '), input('Enter students last name '), id)
            print(database[str(id)].f_name, database[str(id)].l_name + 'is added and id is: ' + str(database[str(id)].student_id))
            id += 1

        # creating a teacher object and adding to the dictionary
        elif student_or_teach == 'teacher':
            database[str(id)] = Teacher(input('Enter the teachers first name '), input('Enter the teachers last name '), id)
            print(database[str(id)].f_name, database[str(id)].l_name + 'is added and id is: ' + str(database[str(id)].staff_id))
            id += 1

        else:
            user_input = 'quit'

    # creating a subject and adding it to the dictionary
    elif user_input == 'subject':
        workshop = MonsterWorkshop(input('Enter the subject name '), input('Enter teacher name '))
        database["Workshops"][workshop.subject] = workshop.teacher
        print(database["Workshops"])

    # adding skill
    elif user_input == 'skill':
        skill_input = input('Enter a skill ')
        which_id = int(input("which id do you want to change "))
        database[str(which_id)].skills.append(skill_input)
        print(database[str(which_id)].f_name, database[str(which_id)].skills)

    # print database
    elif user_input == 'print':
        print(database)

    else:
        user_input='quit'
