factorial = 1

for i in range(1,101):
	factorial *= i
print factorial

sum = 0

for i in str(factorial):
	i = int(i)
	sum += i
	
print sum
	