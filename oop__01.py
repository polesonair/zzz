class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    #  Оценка лекторов поставленная учениками
    def lecturer_grade(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        self.avr_grade = 0  # Средняя оценка
        self.sum_grades = 0  # Сумма оценок
        self.finished_courses_str = 'Нет'
        self.courses_in_progress_str = 'Нет'
        #  Подсчет средней
        if len(self.grades.values()) != 0:
            for i in self.grades.values():
                self.count_lecture = len(i)
                for j in i:
                    self.sum_grades += j
            self.avr_grade = self.sum_grades / self.count_lecture
        else:
            self.avr_grade = 0

        if self.finished_courses:
            self.finished_courses_str = ' '.join(self.finished_courses)
        if self.courses_in_progress:
            self.courses_in_progress_str = ' '.join(self.courses_in_progress)
        out = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avr_grade}\n' \
              f'Курсы в процессе изучения: {self.courses_in_progress_str}\nЗавершенные к' \
              f'урсы: {self.finished_courses_str} '
        return out

    def __lt__(self, other):
        return self.avr_grade < other.avr_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []

    def __str__(self):
        self.avr_grade = 0
        self.sum_grades = 0

        #  Средняя оценка
        if len(self.grades.values()) != 0:
            for i in self.grades.values():
                self.count_lecture = len(i)
                for j in i:
                    self.sum_grades += j
            self.avr_grade = self.sum_grades / self.count_lecture
        else:
            self.avr_grade = 0
        #  Вывод
        out = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avr_grade}'
        return out

    def __lt__(self, other):
        return self.avr_grade < other.avr_grade


class Reviewer(Mentor):
    def __init__(self, name, surname):  # Инициализация
        super().__init__(name, surname)  # Привязка к родительскому классу

    def __str__(self):
        out = f'Имя: {self.name}\nФамилия: {self.surname}'
        return out


#  Средняя оценка
def average_grade(course, *args):
    avr_grade = 0  # Средняя оценка студентов по курсу
    count = 0  # Число студенов по курсу
    temp = 0

    for i in args:
        if i.grades.get(course):  # Если у текущего студента есть данный курс
            sum_grade_current = sum(i.grades[course]) / len(i.grades[course])
            count += 1
            temp += sum_grade_current  # Средняя оценка текущего студента
    if count != 0:  # Если есть студенты в курсе
        avr_grade = temp / count
    print(f'средняя оценка студентов по {course}: {avr_grade}')


#  Средняя оценка по преподавателям
def average_grade_lector(course, *args):
    avr_grade = 0  # Средняя оценка лектора
    count = 0  # число лекторов по курсу
    temp = 0

    for i in args:
        if i.grades.get(course):  # Если у текущего лектора есть этот курс
            sum_grade_current = sum(i.grades[course]) / len(i.grades[course])
            count += 1
            temp += sum_grade_current  # Средняя оценка лектора
    if count != 0:  # Если есть лекторы по курсу
        avr_grade = temp / count
    print(f'средняя оценка лекторов по {course}: {avr_grade}')


#  Студенты
student_1 = Student('Иван', 'Абрамов', 'm')
student_2 = Student('Михаил', 'Галустян', 'm')
student_3 = Student('Стас', 'Старовойтов', 'm')
student_4 = Student('Александр', 'Ревва', 'm')

# Предметы
student_1.courses_in_progress += ['Python']
student_2.courses_in_progress += ['C#']
student_3.courses_in_progress += ['Python']
student_4.courses_in_progress += ['Python']

#  Завершенные курсы
student_1.finished_courses += ['Git']
student_2.finished_courses += ['Git']

#  Эксперты
expert_1 = Reviewer('Владимир', 'Ленин')
expert_2 = Reviewer('Николя', 'Саркози')
expert_3 = Reviewer('Алексей', 'Панин')

#  Предметы экспертов
expert_1.courses_attached += ['Python']
expert_2.courses_attached += ['C#']
expert_3.courses_attached += ['PHP']

#  Лекторы
lector_1 = Lecturer('Юрий', 'Лоза')
lector_2 = Lecturer('Евгений', 'Савин')

#  Предметы лекторов
lector_1.courses_attached += ['Python']
lector_2.courses_attached += ['C#']

#  Оценка студентов экспертами
expert_1.rate_hw(student_1, 'Python', 9)
expert_2.rate_hw(student_2, 'C#', 8)
expert_1.rate_hw(student_1, 'Python', 10)
expert_1.rate_hw(student_4, 'Python', 7)

#  Оценка лекторов студентами
student_1.lecturer_grade(lector_1, 'Python', 10)
student_3.lecturer_grade(lector_1, 'Python', 8)
student_2.lecturer_grade(lector_2, 'C#', 10)

print('Студенты:')
print ('       ')
print(student_1)
print ('       ')
print(student_2)
print ('       ')
print(student_3)
print ('       ')
print(student_4)
print ('       ')

#  Сравнение
print('Сравнение студентов')
if student_1 < student_2:
    print(f'{student_1.name} {student_1.surname} имеет менее высокий бал чем {student_2.name} {student_2.surname}')
else:
    print(f'{student_1.name} {student_1.surname} имеет более высокий бал чем {student_2.name} {student_2.surname}')

print('Лекторы:')
print ('       ')
print(lector_1)
print ('       ')
print(lector_2)
print ('       ')

#  Сравнение 
print('Сравнение лекторов')
if lector_1 < lector_2:
    print(f'{lector_1.name} {lector_1.surname} имеет балл ниже, чем {lector_2.name} {lector_2.surname}')
else:
    print(f'{lector_1.name} {lector_1.surname} имеет балл выше, чем {lector_2.name} {lector_2.surname}')

#  Вывод экспертов
print('Эксперты:')
print ('       ')
print(expert_1)
print ('       ')
print(expert_2)
print ('       ')
print(expert_3)
print ('       ')


average_grade('Python', student_1, student_4, student_2)
average_grade('C#', student_1, student_4, student_2)

average_grade_lector('Python', lector_1, lector_2)
average_grade_lector('C#', lector_1, lector_2)
