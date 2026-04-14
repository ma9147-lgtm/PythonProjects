
NUM_STUDENTS= 3
students_list=[]


for i in range(NUM_STUDENTS):
    student_info = []
    student_info.append(input("Please enter student's name: "))
    student_info.append(input("Please enter student's age: "))
    student_info.append(input("Please enter student's major: "))
    student_info.append(input("Please enter student's graduation year: "))
    students_list.append(student_info)

for student in students_list:
    for info in student:
        print (info,end=" ")

   # print("\n----------")

print(students_list)
