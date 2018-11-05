print("Sup.")

"""
student = {
    "first_name": "Peejee",
    "last_name": "Sattrup",
    "exams":
        {
            "final": 70,
            "midterm": 50,
            "thesis": 100
        },
    "mark":
        [
            12,
            23,
            6,
            67,
            128
        ]
}
"""


# print(student["mark"][1])

# for mark in student["mark"]:
#     print(mark)

# print(student["exams"]["thesis"])

"""
def create_student_list():
    user_input_name = input(str("Yo, gimme the name: "))
    user_input_marks = input("And how 'bout dem marks, separate by commas: ")
    user_marks = user_input_marks.split(",")

    student_data = {
        "name": user_input_name,
        "marks": []
    }

    for marks in user_marks:
        student_data["marks"].append(int(marks))

    return student_data

print(create_student())
"""


def create_student():
    user_input_name = input(str("Yo, gimme the name: "))

    student_data = {
        "name": user_input_name,
        "marks": []
    }

    return student_data


def create_mark(student, mark):
    student["marks"].append(mark)


def calculate_average_mark(student):
    if len(student["marks"]) == 0:
        return 0

    total = sum(student["marks"])
    average = total / len(student["marks"])

    return average


s = create_student()
print(calculate_average_mark(s))
create_mark(s, 2)
print(calculate_average_mark(s))
create_mark(s, 1)
print(calculate_average_mark(s))
create_mark(s, 4)
print(calculate_average_mark(s))
create_mark(s, 2)
print(calculate_average_mark(s))