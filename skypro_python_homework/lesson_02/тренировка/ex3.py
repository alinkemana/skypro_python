from student import Student

from courseGroup import CourseGroup

# Создаем объекты класса Student для ученика и его сокурсников
student = Student("Анна", "Иванова", 25, "Инженер по тестированию")
classmate1 = Student("Иван", "Петров", 27, "Инженер по тестированию")
classmate2 = Student("Мария", "Сидорова", 24, "Инженер по тестированию")
classmate3 = Student("Дмитрий", "Кузнецов", 26, "Инженер по тестированию")

# Создаем объект класса CourseGroup
course_group = CourseGroup(student, [classmate1, classmate2, classmate3])

# Выводим информацию о группе
print(course_group)