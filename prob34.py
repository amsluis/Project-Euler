'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''
import math
answers = []
for i in range(3,math.factorial(9)*7):
    digits = list(str(i))
    total = 0
    for j in digits:
        j = int(j)
        j = math.factorial(j)
        total += j
    if total == i:
        print i
        answers.append(i)
print 'Answer: ', sum(answers)
