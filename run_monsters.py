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

while user_input != 'quit':
    user_input = input("If you want to add a student or teacher type: add \n if you want to add a subject type: subject \n if you want to add a skill: skill \n if you want to print everything: print\n if you want to quit: quit \n")

    # Adding either a student or teacher
    if user_input == 'add':
        student_or_teach = input('input a student or teacher ')

        # Creating a student object and adding it into a dictionary
        if student_or_teach == 'student':
            student = Student(input('Enter the students first name '), input('Enter students last name '), id)
            database[str(id)] = [student.f_name, student.l_name, student.student_id]
            print(student.f_name + ' ' + student.l_name + 'is added and id is: ' + str(student.student_id))
            id += 1

        # Creating a teacher object and and adding it into a dictionary
        elif student_or_teach == 'teacher':
            teacher = Teacher(input('Enter the teachers first name '), input('Enter the teachers last name '), id)
            database[str(id)] = [[student.f_name, student.l_name, student.student_id]]
            print(teacher.f_name + ' ' + teacher.l_name + ' is added and id is: ' + str(teacher.student_id))
            id += 1

        else:
            break

    # Adding a subject
    elif user_input == 'subject':
        workshop = MonsterWorkshop(input('Enter the subject name '), input('Enter teacher name '))
        database["Workshops"][workshop.subject] = workshop.teacher
        print(database["Workshops"])

    # Adding skills into a monster
    elif user_input == 'skill':
        skill_input = input('Enter a skill ')
        which_id = int(input("which id do you want to change "))
        database[str(which_id)].skills.append(skill_input)
        print(database[str(which_id)].f_name, database[str(which_id)].skills)

    # Printing the dictionary
    elif user_input == 'print':
        print(database)

    else:
        break
