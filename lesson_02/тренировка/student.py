class Student:

    def __init__(self, name, surname, age, course):
        self.name = name
        self.surname = surname
        self.age = age
        self.course = course

    def __str__(self):
        return f"{self.name} {self.surname}, {self.age} лет, курс: {self.course}"
