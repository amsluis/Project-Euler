init = 1
triangle = 0
for i in range(1,100000):
	divisors = 0
	triangle += i
	for i in range(1,int(triangle**0.5+1)):
		if triangle % i == 0:
			divisors += 2
		if divisors > 500:
			print triangle
			break
