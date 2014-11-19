'''

'''
import time
from fractions import Fraction
start = time.time()

partial_values = [2]
for i in range(1,34):
    partial_values.append(1)
    partial_values.append(2*i)
    partial_values.append(1)

partial_values.reverse()

previous = 0
for i in partial_values:
    denom = i + previous
    previous = Fraction(1, denom)

number = denom.numerator
answer = 0

for i in str(number):
    answer += int(i)

elapsed = time.time() - start
print 'Answer :',answer,'found in',elapsed,'seconds!'
