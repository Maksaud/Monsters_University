class MonsterWorkshop():
    def __init__(self, subject, teacher):
        self.subject = subject
        self.teacher = teacher
        self.list_attendees = []


    def set_workshops(self):
        the_workshop = []
        the_workshop.append(self.subject)
        the_workshop.append(self.teacher)
        the_workshop.append(self.list_attendees)
        return the_workshop
