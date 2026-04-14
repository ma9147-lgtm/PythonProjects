Num_students= 3
students_list = []




for i in student_info:
	student_info=[]
students_info.append(input("name"))
students_info.append(input("age"))
students_info.append(input("major"))
students_info.append(input("year"))
students_list.append(students_info)

print(students_list)

for student in students_list:
	for info in student:
		print(info, end= ' ')
	print("\n----------------")