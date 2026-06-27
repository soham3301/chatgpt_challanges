student_name_list = []
student_marks_list = []

def get_students():
    number_of_students = int(input("How many students?\n"))
    for counter in range(0, number_of_students):
        student_name_list.append(input("Name: "))
        student_marks_list.append(int(input("Marks: ")))
    return number_of_students

def average_calculator():
    total_mark = 0
    for mark in student_marks_list:
        total_mark += mark
    average_mark = round(total_mark / len(student_marks_list), 2)
    return average_mark

def highest_scorer_name():
    highest_score = student_marks_list[0]
    for score in student_marks_list:
        if highest_score < score:
            highest_score = score
    index_of_highest_score = student_marks_list.index(highest_score)
    name_of_highest_scorer = student_name_list[index_of_highest_score]
    return name_of_highest_scorer

def lowest_scorer_name():
    lowest_score = student_marks_list[0]
    for score in student_marks_list:
        if lowest_score > score:
            lowest_score = score
    index_of_lowest_score = student_marks_list.index(lowest_score)
    name_of_lowest_scorer = student_name_list[index_of_lowest_score]
    return name_of_lowest_scorer

def grade_system(mark):
    if mark >= 80:
        return "Grade A"
    elif mark >= 60:
        return "Grade B"
    elif mark >= 30:
        return "Grade C"
    else:
        return "Fail"

def print_report():
    print("=== REPORT CARD ===")
    for student_details in range(0, len(student_name_list)):
        print(f"{student_name_list[student_details]} : {student_marks_list[student_details]}, {grade_system(student_marks_list[student_details])}")
    print(f"Average Marks: {average_calculator()}")
    print(f"Highest Scorer: {highest_scorer_name()}")
    print(f"Lowest Scorer: {lowest_scorer_name()}")

def main():
    get_students()
    print_report()

main()
