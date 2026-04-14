
student_grades = [['John', '9', '10', '7', '6'],
                  ['Mary', '9', '8', '8'],
                  ['Smith', '8', '4'],
                  ['Adam', '6', '4', '7', '5', '10']]


all_grades_sum=0
all_grades_count=0


for student in student_grades:
	for item in student:
		print(item,end= ' ')
	print('\n--------------')

for student in student_grades:
    grades_sum=0
    count=0
    for grades in student[1:]: 
        grades_sum = grades_sum + int(grades)
        all_grades_sum = all_grades_sum +int(grades)
        count = count + 1 
        all_grades_count = all_grades_count + 1
    print ('the average for', student[0], 'is', grades_sum/count)

print('The average for all students is', all_grades_sum/all_grades_count)

