class StudentsInMLOps:
    def __init__(self):
        self.students = 0
        self.className = "StudentsInMLOps"

    def enrollStudents(self, count):
        self.students += count

    def dropStudents(self, count):
        self.students -= count

    def getTotalStrength(self):
        return self.students

    def getClassName(self):
        return self.className
