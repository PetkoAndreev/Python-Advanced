number = int(input())


def input_students_grades(number):
    students_grades = {}
    for _ in range(number):
        student, grade = input().split()
        if student not in students_grades:
            students_grades[student] = []
        students_grades[student].append(float(grade))
    return students_grades


def avg_grades(values):
    return sum(values) / len(values)

def print_data(students_grades):
    for student, grades in students_grades.items():
        grades_str = " ".join(map(lambda grade: f"{grade:.2f}", grades))
        avg_grade = avg_grades(grades)
        print(f'{student} -> {grades_str} (avg: {avg_grade:.2f})')


students_grades = input_students_grades(number)
print_data(students_grades)