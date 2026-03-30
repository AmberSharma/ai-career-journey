class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.name}: {self.marks}"

    def average(self):
        return sum(self.marks) / len(self.marks)


obj = Student("Amber", [70, 80, 90, 100])
print(obj)
print(obj.name)
print(obj.marks)
print(obj.average())