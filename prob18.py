triangle = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

# Organize the data.

a = triangle.split('\n')
data = []
for i in a:
	b = i.split()
	sublist = []
	for i in b:
		i = int(i)
		sublist.append(i)
	data.append(sublist)


# Work from the bottom of the triangle, up.
# 


for i in range(len(data) - 1):
	node_row = data[-i - 2]
	print 'input row', data[-i - 2]
	temp = []
	for j in range(len(node_row)):
		node_element = node_row[j]
		branch_row = data[-i - 1]
		branch_element1 = branch_row[j]
		branch_element2 = branch_row[j + 1]
		sum1 = node_element + branch_element1
		sum2 = node_element + branch_element2
		if sum1 > sum2:
			temp.append(sum1)
		else:
			temp.append(sum2)
		print 'temp buffer', temp
	data[-i - 2] = temp
	
print data








