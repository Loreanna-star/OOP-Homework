class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {} #это словарь с наполнением: курс:оценка

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if grade >=0 and grade <=10:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return "Ошибка"
        else:
            return "Ошибка"

        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"
 
# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
 
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
 
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
 
# print(best_student.grades)

vasily_pupkin = Student("Vasily", "Pupkin", "male")
vasily_pupkin.courses_in_progress += ['Python']

anna_chicken = Student("Anna", "Chicken", "female")
anna_chicken.courses_in_progress += ['Java']

alex_ivanov = Lecturer("Alex", "Ivanov")
alex_ivanov.courses_attached += ['Java']

elena_petrova = Lecturer("Elena", "Petrova")
elena_petrova.courses_attached += ['Python']

petr_sidorov = Reviewer("Petr", "Sidorov")
petr_sidorov.courses_attached += ['Java']

andrey_medvedev = Reviewer("Andrey", "Medvedev")
andrey_medvedev.courses_attached += ['Python']

vasily_pupkin.rate_lecture(elena_petrova, "Python", 7)

anna_chicken.rate_lecture(alex_ivanov, "Java", 9)

petr_sidorov.rate_hw(anna_chicken, "Java", 2)

andrey_medvedev.rate_hw(vasily_pupkin, "Python", 4)


print("Курсы, которые ведет Алекс Иванов", alex_ivanov.courses_attached)
print("Курсы, которые ведет Елена Петрова", elena_petrova.courses_attached)
print("Оценки, которые получил студент Василий Пупкин", vasily_pupkin.grades)
print("Оценки, которые получила студентка Анна Чикен", anna_chicken.grades)
print("Оценки, которые получил лектор Елена Петрова", elena_petrova.grades)
print("Оценки, которые получил лектор Алекс Иванов", alex_ivanov.grades)
print()

