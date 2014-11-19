def abundant(number):
	divs = []
	for i in range(1,number/2+1):
		if number % i == 0:
			divs.append(i)
	sum = 0
	print divs
	for i in divs:
		sum += int(i)
	print sum
	if sum > number:
		return number
	else:
		pass
		
abundant(18)