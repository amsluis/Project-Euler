'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
import time

start = time.time()

upto = 28000

def abundant(number):
	divs = []
	for i in range(1,number/2+1):
		if number % i == 0:
			divs.append(i)
	sum = 0
	for i in divs:
		sum += int(i)
	if sum > number:
		return number
	else:
		pass


a = []
for i in range(1,upto + 1):
	b = abundant(i)
	if b:
		a.append(b)
print '\n',a,'\n'

seive = [False] * (upto - 1)
for i in a:
	if i <= upto:
		#seive[i+1] = True
		for j in a:
			sum = i + j
			if sum <= upto - 2:
				seive[sum] = True
				
answer = 0

print seive

for i in range(len(seive)):
	if seive[i] == False:
		answer += i
	
print answer, '\n'













