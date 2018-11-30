#Author: Jake Herman
#Section: C
#Description: takes in assignment grades of many students and calculates their personal average
#             as well as the class average for each assignment.

students = {} # dictionary storing student data {id: {name: , scores: []}}
continue_choice = 'y'

def add_student():
    #input is fed directly into the dictionary. student name first.
    students[input("enter student's id: ")] = {"name":str(input("enter student's name: "))}

while continue_choice == 'y':
    #prompts the user to input student info
    add_student()
    continue_choice = input("would you like to enter another student (y/n)?")

for student_id in students.keys():
    print("enter scores for {}".format(students[student_id]["name"]))
    scores = []

    for i in range(1,4):
        score = -1
        #checks to make sure that the user inputs a valid score in
        while score > 100 or score < 0:
            score = int(input("enter scores for assignment {} (0-100)".format(i)))
        scores.append(score)

    students[student_id]["scores"] = scores

print("final grade report: ")

for student_id in students.keys():
    student_scores = students[student_id]["scores"]
    #the sum function adds all elements in a list, using to calculate average
    print("{}'s average score was: {}".format(students[student_id]["name"], sum(student_scores)/len(student_scores)))

print("assignment averages: ")

scores = []

for i in range(0,3):
    student_scores = []
    for student_id in students.keys():
        #puts list inside of list. each list contains students' scores for each assignment.
        student_scores.append(students[student_id]["scores"][i])
    scores.append(student_scores)

for idx, score in enumerate(scores):
    print("average for assignment {} was {}".format(idx+1, sum(score)/len(score)))
