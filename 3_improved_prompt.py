# Read students and GPAs from a file
students = []
gpas = []

with open("students.txt", "r") as file:
    for line in file:
        name, gpa = line.strip().split()
        students.append(name)
        gpas.append(float(gpa))

# Compute average GPA
average_gpa = sum(gpas) / len(gpas)
print(f"Average GPA: {average_gpa:.2f}")

# Print students with above-average GPA
print("Above-average students:")
for i in range(len(students)):
    if gpas[i] > average_gpa:
        print(f"{students[i]}: {gpas[i]}")

# Predict scholarships (example: GPA >= 3.0)
print("Students predicted to earn scholarships:")
for i in range(len(students)):
    if gpas[i] >= 3.0:
        print(f"{students[i]}: {gpas[i]}")