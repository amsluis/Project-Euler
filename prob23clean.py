import time

start = time.time()

def divisors(number):
	divs = []
	for i in range(1,number/2+1):
		if number % i == 0:
			divs.append(i)
	sum = 0
	for i in divs:
		sum += int(i)
	return sum
	
upto = 28000
solution = 0

abundants = set()

for n in range(upto):
	if divisors(n) > n:
		abundants.add(n)
	if not any((n-i in abundants) for i in abundants):
		print n
		solution += n
		
elapsed = time.time() - start
		
print 'Solution: ', solution, ' found in ', elapsed, ' seconds'