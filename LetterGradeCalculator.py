t = True
sid_list = []
midterm_list = []
quiz_list = []
final_list = []
grade_list = []
average=60
total_grade = 0
letter_list= []

while t:
    letter_grade=""
    sid = int(input("student id: "))
    midterm = float(input("Midterm: "))
    while midterm not in range(0, 101):
        print("Incorrect grade entry, please enter a grade between 0-100.")
        midterm = float(input("Please enter the midterm grade:"))
    quiz = float(input("quiz: "))
    while quiz not in range(0, 101):
        print("Incorrect grade entry, please enter a grade between 0-100.")
        quiz = float(input("Please enter the quiz grade:"))
    final = float(input("final: "))
    while final not in range(0, 101):
        print("Incorrect grade entry, please enter a grade between 0-100.")
        final = float(input("Please enter the final grade:"))
    grade = quiz * 0.2 + midterm * 0.3 + final * 0.5
    if grade < 50:
        letter_grade = "FF"
    elif grade < 60:
        letter_grade = "FD"
    elif grade < 65:
        letter_grade = "DD"
    elif grade < 70:
        letter_grade = "DC"
    elif grade < 75:
        letter_grade = "CC"
    elif grade < 80:
        letter_grade = "CB"
    elif grade < 85:
        letter_grade = "BB"
    elif grade < 90:
        letter_grade = "BA"
    else:
        letter_grade = "AA"

    sid_list.append(sid)
    midterm_list.append(midterm)
    quiz_list.append(quiz)
    final_list.append(final)
    grade_list.append(grade)
    letter_list.append(letter_grade)
    total_grade = total_grade + grade
    q = input("Another student? (Y) or (N)?: ")
    if q == "N":
        t = False
avg = total_grade / len(sid_list)

print("General Average: ", avg)
for i in range(len(sid_list)):
    note = ""
    if grade_list[i] < avg:
        note = "Failed"
    else:
        note = "Passed"
    print(str(i+1),".Student =>" + '\t' + str(midterm_list[i]) + '\t' + str(quiz_list[i]) + '\t' + str(
        final_list[i]) + '\t' + str(grade_list[i]) + '\t' + note,"with",letter_list[i])