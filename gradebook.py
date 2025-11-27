# Name: Vansh Ahuja
# Date: 27 Nov 2025
# Title: GradeBook Analyzer - Mini Project

import csv

def calculate_average(marks_dict):
    values = list(marks_dict.values())
    return sum(values) / len(values)

def calculate_median(marks_dict):
    values = sorted(marks_dict.values())
    n = len(values)
    if n % 2 == 1:
        return values[n // 2]
    else:
        return (values[n//2 - 1] + values[n//2]) / 2

def find_max_score(marks_dict):
    return max(marks_dict.values())

def find_min_score(marks_dict):
    return min(marks_dict.values())


while True:
    print("\nWelcome to GradeBook Analyzer")
    print("1. Manual Input")
    print("2. Load from CSV")

    choice = int(input("Choose option: "))

    marks = {}

    #  Manual Entry 
    if choice == 1:
        count = int(input("How many students? "))
        for i in range(count):
            name = input("Enter student name: ")
            score = int(input("Enter marks: "))
            marks[name] = score

    #  CSV Entry 
    elif choice == 2:
        filename = input("Enter CSV filename: ")
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)       
            for row in reader:
                name = row[0]
                score = int(row[1])
                marks[name] = score

    else:
        print("Invalid choice!")
        continue


    #  Grade Assignment 
    grades = {}

    for name, score in marks.items():
        if score >= 90:
            grades[name] = "A"
        elif score >= 80:
            grades[name] = "B"
        elif score >= 70:
            grades[name] = "C"
        elif score >= 60:
            grades[name] = "D"
        else:
            grades[name] = "F"

    #  Grade Distribution 
    count_A = list(grades.values()).count("A")
    count_B = list(grades.values()).count("B")
    count_C = list(grades.values()).count("C")
    count_D = list(grades.values()).count("D")
    count_F = list(grades.values()).count("F")

    print("\nGrade Distribution:")
    print("A:", count_A)
    print("B:", count_B)
    print("C:", count_C)
    print("D:", count_D)
    print("F:", count_F)

    #  Pass / Fail Lists 
    passed_students = [name for name, score in marks.items() if score >= 40]
    failed_students = [name for name, score in marks.items() if score < 40]

    print("\nPassed Students:", passed_students)
    print("Failed Students:", failed_students)

    # Table Output 
    print("\nName\tMarks\tGrade")
    print("-----")
    for name in marks:
        print(f"{name}\t{marks[name]}\t{grades[name]}")

    # Ask to Run Again 
    run = input("\nRun again? (y/n): ")
    if run.lower() == "n":
        break