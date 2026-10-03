# list of three students named Jon, Kim, and Lee
students = ["Jon", "Kim", "Lee"]
students.extend(["Sara", "Miko"])
# change Jon to John
students[0] = 'John'
# function to print 'Hi name' for each student in the list
def print_greetings(student_list):
    for name in student_list:
        print(f"Hi {name}")
    print(f"Total number of students: {len(student_list)}")

# call the function
print_greetings(students)