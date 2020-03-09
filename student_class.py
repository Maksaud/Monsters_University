from monsters_class import *


class Student(Monsters):
    def __init__(self, f_name, l_name, student_id):
        super().__init__(f_name, l_name)
        self.student_id = student_id
