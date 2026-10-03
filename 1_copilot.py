# list of three students named Jon, Kim, and Lee
students = ["Jon", "Kim", "Lee"]

# function to print 'Hi name' for each student in the list
def print_greetings(student_list):
    for name in student_list:
        print(f"Hi {name}")

# call the function
print_greetings(students)