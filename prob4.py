answer = []

for i in range(100,1000):
	for j in range(i,1000):
		candidate = str(i*j)
		if candidate == candidate[::-1]:
			answer.append(int(candidate))
			
print max(answer)