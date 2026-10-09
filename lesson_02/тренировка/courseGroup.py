class CourseGroup:

    def __init__(self, student, classmates):
        print()
        self.student = student
        self.classmates = classmates

    def __str__(self):
        classmates_str = ", ".join([str(classmate) for classmate in self.classmates])
        return f"{self.student} учится вместе с: {classmates_str}"