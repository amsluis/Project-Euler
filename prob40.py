'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
'''
import time
start = time.time()
Champernowne = ''
answer = 1

for i in range(1,1000000):
    Champernowne += str(i)
for i in range(7):
    index = 10**i
    digit = Champernowne[index - 1]
    answer *= int(digit)

elapsed = time.time() - start
print 'Answer :', answer, ' found in ', elapsed, ' seconds!'
