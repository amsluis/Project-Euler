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
	
SumList = []
Amicable = []
for i in range(1,10000):
	a = divisors(i)
	if divisors(a) == i and a != i:
		Amicable.append(i)

print '\nThese are the Amicable Numbers: %r' % Amicable
print 'Which add to: %r\n' % sum(Amicable)

elapsed = (time.time() - start)

print 'Answer found in %s seconds\n' % elapsed