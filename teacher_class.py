from monsters_class import *

class Teacher(Monsters):
    def __init__(self, f_name, l_name, staff_id):
        super().__init__(f_name, l_name)
        self.staff_id = staff_id
