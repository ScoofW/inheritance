class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_lecturer (self,lecturer,course,grade):
        if course in self.courses_in_progress and lecturer in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __lt__ (self,other):
        return self.get_average_grade() < other.get_average_grade()
    
    def __le__ (self,other):
        return self.get_average_grade() <= other.get_average_grade()
    
    def __gt__ (self,other):
        return self.get_average_grade() > other.get_average_grade()
    
    def __ge__ (self,other):
        return self.get_average_grade() >= other.get_average_grade()
    
    def get_average_grade(self):
        total_grades = sum([sum(grades) for grades in self.grades.values()])
        total_count = sum([len(grades) for grades in self.grades.values()])  
        return total_grades / total_count if total_count > 0 else 0
          
    def __str__(self):
        in_progress = ', '.join(self.courses_in_progress)
        finished = ','.join(self.finished_courses)
        return f"Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашние задания: {self.get_average_grade():.1f}\n Курсы в процессе изучения: {in_progress}\n Завершенные курсы: {finished}"
        
                    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def get_average_grade(self):
        total_grades = sum([sum(grades) for grades in self.grades.values()])
        total_count = sum([len(grades) for grades in self.grades.values()])
        return total_grades / total_count if total_count > 0 else 0
    
    def average_lecture_grade(self, course):
        total_grades = 0
        total_count = 0
        for lecturer in lecturers:
            if course in lecturer.grades:
                total_grades += sum(lecturer.grades[course])
                total_count += len(lecturer.grades[course])
        return total_grades / total_count if total_count > 0 else 0
    
    def __lt__ (self,other):
        return self.get_average_grade() < other.get_average_grade()
    
    def __le__ (self,other):
        return self.get_average_grade() <= other.get_average_grade()
    
    def __gt__ (self,other):
        return self.get_average_grade() > other.get_average_grade()
    
    def __ge__ (self,other):
        return self.get_average_grade() >= other.get_average_grade()
    
    def __str__(self):
        average_grade = sum([sum(grades) / len(grades) for grades in self.grades.values()]) / len(self.grades.values())
        return f"Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {average_grade:.1f}"
        
 
class Reviewer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f"Имя: {self.name}\n Фамилия: {self.surname}"
    
    def average_hw_grade(self ,course):
        total_grades = 0
        total_count = 0
        for student in students:
            if course in student.grades:
                total_grades += sum(student.grades[course])
                total_count += len(student.grades[course])
        return total_grades / total_count if total_count > 0 else 0


student1 = Student('Ruoy', 'Eman', 'male')
student2 = Student('Alice', 'Smith', 'female')
lecturer1 = Lecturer('John', 'Doe')
lecturer2 = Lecturer('Jane', 'Johnson')

reviewer1 = Reviewer('Reviewer1', 'Eman')
reviewer2 = Reviewer('Reviewer2', 'Smith')

student1.courses_in_progress = ['Python', 'Git']
student1.finished_courses = ['Введение в программирование']

student2.courses_in_progress = ['Python', 'Git']
student2.finished_courses = ['Введение в программирование']

# Задаем оценки
student1.grades = {'Python': [9, 8, 5], 'Git': [10, 6, 7]}
student2.grades = {'Python': [9, 10, 8], 'Git': [4, 8, 6]}

lecturer1.grades = {'Python': [7, 8, 7], 'Git': [10, 8, 7]}
lecturer2.grades = {'Python': [7, 6, 10], 'Git': [8, 5, 9]}

# Создаем список студентов и лекторов
students = [student1, student2]
lecturers = [lecturer1, lecturer2]
reviewers = [reviewer1, reviewer2]

# Вызываем функции для подсчета средних оценок
average_hw_python = reviewer1.average_hw_grade('Python')
average_hw_git = reviewer1.average_hw_grade('Git')
average_lecture_python = lecturer1.average_lecture_grade('Python')
average_lecture_git = lecturer1.average_lecture_grade('Git')

# Выводим результаты
print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(student1 < student2)
print(lecturer1 > lecturer2)

print(f"Средняя оценка за домашние задания по Python: {average_hw_python:.2f}")
print(f"Средняя оценка за домашние задания по Git: {average_hw_git:.2f}")
print(f"Средняя оценка за лекции по Python: {average_lecture_python:.2f}")
print(f"Средняя оценка за лекции по Git: {average_lecture_git:.2f}")