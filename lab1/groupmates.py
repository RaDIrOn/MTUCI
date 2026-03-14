#coding:utf-8
groupmates = [
    {
        "name": u"Максим",
        "group": "2254",
        "age": 25,
        "marks": [4, 3, 5, 5, 4]
    },
    {
        "name": u"Анна",
        "group": "2254",
        "age": 24,
        "marks": [5, 5, 5, 4, 3]
    },
    {
        "name": u"Вадим",
        "group": "2254",
        "age": 24,
        "marks": [3, 5, 4, 3, 5]
    },
    {
        "name": u"Вика",
        "group": "2254",
        "age": 23,
        "marks": [5, 5, 5, 4, 5]
    }
]

def print_students(students):
    print u"Имя студента".ljust(15), \
        u"Группа".ljust(8), \
        u"Возраст".ljust(8), \
        u"Оценки".ljust(20)
    for student in students:
        print student["name"].ljust(15), \
            student["group"].ljust(8), \
            str(student["age"]).ljust(8), \
            str(student["marks"]).ljust(20)
    print "\n"

print_students(groupmates)

def filter_avg(students, min_avg):
    filtered_students = []
    for student in students:
        avg_mark = sum(student["marks"]) / len(student["marks"])
        if avg_mark >= min_avg:
            filtered_students.append(student)
    return filtered_students

print u"Студенты со средним баллом >= 4:"
filtered = filter_avg(groupmates, 4)
print_students(filtered)