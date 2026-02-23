import csv
import random

# =========================
# Step 1: Generate test data CSV
# =========================
with open("students_test.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "GPA", "Major"])
    majors = ["Math", "Biology"]
    for i in range(20):  # generate 20 random students
        name = f"Student{i+1}"
        gpa = round(random.uniform(1.0, 4.0), 2)
        major = random.choice(majors)
        writer.writerow([name, gpa, major])

print("Test data CSV 'students_test.csv' created.")

# =========================
# Step 2: Read CSV into dictionary
# =========================
students = {}
with open("students_test.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        students[row["Name"]] = (float(row["GPA"]), row["Major"])

# =========================
# Step 3: Compute average GPA
# =========================
total_gpa = sum(gpa for gpa, major in students.values())
average_gpa = total_gpa / len(students)
print(f"\nAverage GPA: {average_gpa:.2f}")

# =========================
# Step 4: Print above-average students
# =========================
print("Above-average students:")
for name, (gpa, major) in students.items():
    if gpa > average_gpa:
        print(f"{name}: {gpa}")

# =========================
# Step 5: Predict scholarships (step-by-step)
# =========================
print("Students predicted to earn scholarships:")
for name, (gpa, major) in students.items():
    if major == "Math" and gpa >= 3.5:
        print(f"{name}: {gpa}")
    elif major == "Biology" and gpa >= 2.75:
        print(f"{name}: {gpa}")