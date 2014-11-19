
answer = 0
for i in range(1,1000000):
	j = i
	count = 0
	while j != 1:
		if j % 2 == 0:
			j = j/2
			count += 1
			pass
		elif j % 2 != 0:
			j = 3*j + 1
			count += 1
			pass
		elif j == 1:
			count +=1
			break
	if count > answer:
		answer = count
		print i
		print answer




