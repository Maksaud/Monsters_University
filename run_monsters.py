from teacher_class import *
from student_class import *
from monsters_class import *
from monster_workshops import *

# Creating a student
student1 = Student('Maksaud', 'Ahmed', 1)

list_of_student = []

# A list of students
list_of_student.append(student1)

# Creating workshops
workshop1 = MonsterWorkshop('Maths', 'mr man')
workshop2 = MonsterWorkshop('English', 'mr woman')

# Listing workshops
list_of_workshop = []
 # Putting each set of workshops into the list.
list_of_workshop.append(workshop1.set_workshops()) # subject
list_of_workshop.append(workshop2.set_workshops())

print(list_of_workshop)

# Creating a list of skills
student1.skills.append('stealth')
student1.skills.append('streangth')

# Printing all skiils of students
print(student1.skills)
