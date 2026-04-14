cnt=1
outer_list=[]
for r in range(3):
	row_list=[]
	for c in range(3):
		row_list.append(cnt)
		cnt=cnt+1
	outer_list.append(row_list)

	print(outer_list)