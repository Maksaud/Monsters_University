from monsters_class import *


class Student(Monsters):
    def __init__(self, f_name, l_name, skills, student_id):
        super().__init__(f_name, l_name, skills)
        self.student_id
