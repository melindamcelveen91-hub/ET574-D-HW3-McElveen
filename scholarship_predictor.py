import csv

# Store each student's major and GPA in a dictionary.
students = {}

# The CSV file should be saved in the same folder as this program.
with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["name"].strip()
        major = row["major"].strip()
        gpa = float(row["gpa"])

        if 0.0 <= gpa <= 4.0:
            students[name] = {"major": major, "gpa": gpa}
        else:
            print("Skipping", name, "because the GPA is out of range.")

# Calculate the average GPA.
total_gpa = 0
for student in students.values():
    total_gpa += student["gpa"]

if len(students) > 0:
    average_gpa = total_gpa / len(students)
    print(f"Average GPA: {average_gpa:.2f}")

    print("\nStudents above the average GPA:")
    for name, student in students.items():
        if student["gpa"] > average_gpa:
            print(f"{name}: {student['gpa']:.2f} ({student['major']})")

    print("\nScholarship predictions:")
    for name, student in students.items():
        major = student["major"].lower()
        gpa = student["gpa"]

        # Hypothesis based on the six examples, not a proven rule:
        # Biology majors qualify; Math majors qualify at GPA >= 3.50.
        if major == "biology":
            prediction = "Predicted scholarship"
        elif major == "math" and gpa >= 3.50:
            prediction = "Predicted scholarship"
        elif major == "math":
            prediction = "Predicted no scholarship"
        else:
            prediction = "Unknown (not enough examples for this major)"

        print(f"{name}: {prediction}")
else:
    print("No students with valid GPAs were found.")
