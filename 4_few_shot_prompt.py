# Store students and GPAs in lists
students = ["Jon", "Kim", "Lee", "Sara", "Miko", "Lin", "Toby", "Ben", "Mark", "Xia"]
gpas = [3.25, 2.25, 2.30, 4.00, 1.90, 2.10, 2.89, 2.75, 2.34, 3.53]

# Compute average GPA
average_gpa = sum(gpas) / len(gpas)
print(f"Average GPA: {average_gpa:.2f}")

# Print above-average students
print("Above-average students:")
for i in range(len(students)):
    if gpas[i] > average_gpa:
        print(f"{students[i]}: {gpas[i]}")

# Predict scholarships based on example threshold (>= 2.75 GPA)
print("Students predicted to earn scholarships:")
for i in range(len(students)):
    if gpas[i] >= 2.75:
        print(f"{students[i]}: {gpas[i]}")