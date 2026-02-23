# list of three students named Jon, Kim and Lee
students = ['Jon', 'Kim', 'Lee']
# add two more students after the list is created
students.append('Sara')
students.append('Miko')
# change Jon to John
students[0] = 'John'
# function to print ‘Hi name’ for each student in the list
def greet_students(student_list):
    for student in student_list:
        print(f'Hi {student}')
    # print the total number of students
    print(f'Total students: {len(student_list)}')
# call the function
greet_students(students)