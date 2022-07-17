###  Задание 1-3

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {} 

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if grade >=0 and grade <=10:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return "Неверный балл"
        else:
            return "Ошибка"

    def _average_grade(self):
        total = 0
        counter = 0
        for value in self.grades.values():
            for grade in value:
                total += grade
                counter += 1
        average = round(total / counter, 2)
        return average

    def __str__(self):
        res =  (
        f'Имя: {self.name}\n'
        f'Фамилия: {self.surname}\n'
        f'Средняя оценка за домашние задания: {self._average_grade()}\n'
        f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
        f'Завершенные курсы: {", ".join(self.finished_courses)}'
        )
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Некорректное сравнение")
            return
        return self._average_grade() < other._average_grade()


        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_grade(self):
        total = 0
        counter = 0
        for value in self.grades.values():
            for grade in value:
                total += grade
                counter += 1
        average = round(total / counter, 2)
        return average

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_grade()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Некорректное сравнение")
            return
        return self._average_grade() < other._average_grade()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

### Задание 4

# Создадим преподавателей, студентов, заполним информацию о курсах и о выставленных оценках

vasily_pupkin = Student("Vasily", "Pupkin", "male")
vasily_pupkin.courses_in_progress += ['Python']
vasily_pupkin.courses_in_progress += ['Git']
vasily_pupkin.finished_courses = ['C++']

anna_chicken = Student("Anna", "Chicken", "female")
anna_chicken.courses_in_progress += ['Java']
anna_chicken.courses_in_progress += ['Git']
anna_chicken.finished_courses = ['JS']

alex_ivanov = Lecturer("Alex", "Ivanov")
alex_ivanov.courses_attached += ['Java']
alex_ivanov.courses_attached += ['Git']

elena_petrova = Lecturer("Elena", "Petrova")
elena_petrova.courses_attached += ['Python']

petr_sidorov = Reviewer("Petr", "Sidorov")
petr_sidorov.courses_attached += ['Java']

andrey_medvedev = Reviewer("Andrey", "Medvedev")
andrey_medvedev.courses_attached += ['Python']
andrey_medvedev.courses_attached += ['Git']

vasily_pupkin.rate_lecture(elena_petrova, "Python", 7)  # одну лекцию Елена рассказала лучше
vasily_pupkin.rate_lecture(elena_petrova, "Python", 6)  # а вторую хуже =((
vasily_pupkin.rate_lecture(alex_ivanov, "Git", 9)

anna_chicken.rate_lecture(alex_ivanov, "Java", 9)
anna_chicken.rate_lecture(alex_ivanov, "Java", 10)
anna_chicken.rate_lecture(alex_ivanov, "Git", 8)

petr_sidorov.rate_hw(anna_chicken, "Java", 2)
petr_sidorov.rate_hw(anna_chicken, "Java", 1)

andrey_medvedev.rate_hw(vasily_pupkin, "Git", 4)
andrey_medvedev.rate_hw(anna_chicken, "Git", 3)

andrey_medvedev.rate_hw(vasily_pupkin, "Python", 4)
andrey_medvedev.rate_hw(vasily_pupkin, "Python", 3)

#Выведем информацию (списки курсов и словари оценок выведены для удобства и контроля)

print(vasily_pupkin)
print("Оценки, которые получил студент Василий Пупкин:", vasily_pupkin.grades)
print(anna_chicken)
print("Оценки, которые получила студентка Анна Чикен:", anna_chicken.grades)

print(vasily_pupkin < anna_chicken)

print(alex_ivanov)
print("Курсы, которые ведет Алекс Иванов:", alex_ivanov.courses_attached)
print("Оценки, которые получил лектор Алекс Иванов:", alex_ivanov.grades)

print(elena_petrova)
print("Курсы, которые ведет Елена Петрова:", elena_petrova.courses_attached)
print("Оценки, которые получил лектор Елена Петрова:", elena_petrova.grades)

print(alex_ivanov < elena_petrova)

print(petr_sidorov)
print(andrey_medvedev)

# Функции

students = [vasily_pupkin, anna_chicken]
lecturers = [alex_ivanov, elena_petrova]

def total_average_hw(students_list, course):
    sum_ = 0
    count = 0
    
    for student in students_list:
        if course not in student.grades.keys():
            continue
        else:
            for grade in student.grades[course]:
                count += 1
                sum_ += grade
    result = sum_ / count

    return result

print(total_average_hw(students, "Git"))
print(total_average_hw(students, "Java"))
print(total_average_hw(students, "Python"))

def total_average_grade(lecturers_list, course):
    sum_ = 0
    count = 0
    
    for lecturer in lecturers_list:
        if course not in lecturer.grades.keys():
            continue
        else:
            for grade in lecturer.grades[course]:
                count += 1
                sum_ += grade
    result = sum_ / count

    return result

print(total_average_grade(lecturers, "Git"))
print(total_average_grade(lecturers, "Python"))
print(total_average_grade(lecturers, "Java"))

