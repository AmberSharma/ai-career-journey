student_marks = {
    'Alex': 80,
    'Bob': 90,
    'Charlie': 70,
    'David': 60,
    'Eve': 50,
    'Frank': 40,
}
max_marks = 0
max_student = ''
for student,mark in student_marks.items():
    if (max_marks < mark):
        max_marks = mark
        max_student = student

print(max_student, max_marks)