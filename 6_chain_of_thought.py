# Dictionary of students: key=name, value=(GPA, Major)
students = {
    "Jon": (3.25, "Math"),
    "Kim": (2.25, "Biology"),
    "Lee": (2.30, "Math"),
    "Sara": (4.00, "Math"),
    "Miko": (1.90, "Math"),
    "Lin": (2.10, "Biology"),
    "Toby": (2.89, "Biology"),
    "Ben": (2.75, "Math"),
    "Mark": (2.34, "Math"),
    "Xia": (3.53, "Biology")
}

# Compute average GPA
total_gpa = sum(gpa for gpa, major in students.values())
average_gpa = total_gpa / len(students)
print(f"Average GPA: {average_gpa:.2f}")

# Print students above average
print("Above-average students:")
for name, (gpa, major) in students.items():
    if gpa > average_gpa:
        print(f"{name}: {gpa}")

# Predict scholarships using step-by-step logic
print("Students predicted to earn scholarships:")
for name, (gpa, major) in students.items():
    # Step-by-step rules
    if major == "Math" and gpa >= 3.5:
        print(f"{name}: {gpa}")
    elif major == "Biology" and gpa >= 2.75:
        print(f"{name}: {gpa}")