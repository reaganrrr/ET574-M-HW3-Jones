# list of three students named Jon, Kim and Lee
students = ['Jon', 'Kim', 'Lee']
# function to print ‘Hi name’ for each student in the list
def greet_students(student_list):
    for student in student_list:
        print(f'Hi {student}')
# call the function
greet_students(students)