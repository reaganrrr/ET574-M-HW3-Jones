# Students and GPAs using delimiters
###list data: Jon 3.25, Kim 2.25, Lee 2.30, Sara 4.00, Miko 1.90, Lin 2.10, Toby 2.89, Ben 2.75, Mark 2.34, Xia 3.53
###

# Convert the list into Python lists
data_string = "Jon 3.25, Kim 2.25, Lee 2.30, Sara 4.00, Miko 1.90, Lin 2.10, Toby 2.89, Ben 2.75, Mark 2.34, Xia 3.53"

# Parse the data
students = []
gpas = []

for item in data_string.split(", "):
    name, gpa = item.split(" ")
    students.append(name)
    gpas.append(float(gpa))

# Compute average GPA
average_gpa = sum(gpas) / len(gpas)
print(f"Average GPA: {average_gpa:.2f}")

# Print above-average students
print("Above-average students:")
for i in range(len(students)):
    if gpas[i] > average_gpa:
        print(f"{students[i]}: {gpas[i]}")

# Predict scholarships (>= 2.75 GPA)
print("Students predicted to earn scholarships:")
for i in range(len(students)):
    if gpas[i] >= 2.75:
        print(f"{students[i]}: {gpas[i]}")