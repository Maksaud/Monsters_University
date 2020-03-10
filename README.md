# Monsters University :taco:

## User Stories
- As a receptionist of the university, I should be able to create a student

- As a receptionist of the university, I should be able to create a teacher

- As a receptionist of the university, I should be able to list all workshops

- As a receptionist of the university, I should be able to create a workshops

- As a receptionist of the university, I should be able to add skills to a student object

- As a receptionist of the uni, I should be able to list all of the student's skills

## Classes
- Monsters Classes
- Student Classes - Child of Monsters
- Teacher class - child of Monsters
- MonsterWorkshop class

### Attributes
- f_name
- l_name
- skills
- list_attendees
- student_id
- teacher_id
- subject


### Method for  list of workshops
- Method for bunching the details of the workshops
```python
def set_workshops(self):
      the_workshop = []
      the_workshop.append(self.subject)
      the_workshop.append(self.teacher)
      the_workshop.append(self.list_attendees)
      return the_workshop
```

# Initialisation

```
git clone https://github.com/Maksaud/Monsters_University.git
```
to run
```
python3 run_monsters.py
```
