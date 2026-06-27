# Finding total no of students
students_no = int(input("How many studens in total: "))

# Finding about their name and marks
student_name_list = []
student_marks_list = []
for _ in range(0, students_no):
    student_name = str(input("Enter the name of the student: "))
    student_marks = int(input("Enter his / her marks: "))
    student_name_list.append(student_name)
    student_marks_list.append(student_marks)

# Finding the heghest score
highest_score = 0
for score_counter in range(0, len(student_marks_list)):
    if highest_score < student_marks_list[score_counter]:
        highest_score = student_marks_list[score_counter]
index_of_highest_score = student_marks_list.index(highest_score)
name_of_the_highest_scorer = student_name_list[index_of_highest_score]

# Finding the average
total_score = 0
for score_counter in student_marks_list:
    total_score += score_counter
average_score = round(total_score / len(student_marks_list))

print("===== REPORT =====")
for student_index in range(0, len(student_name_list)):
    print(f"{student_name_list[student_index]} : {student_marks_list[student_index]}")
print(f"Highest Score : {name_of_the_highest_scorer}\n"f"Average : {average_score}")
