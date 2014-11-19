'''

'''
import time
start = time.time()

def Pentagonal(n):
    a = []
    for i in range(1,n+1):
        i = i*(3*i-1)/2
        a.append(i)
    return a

numbers = Pentagonal(10000)
numbers_set = set(numbers)
answer = 1000000000

for i in numbers:
    for j in numbers:
        a = i+j
        b = i-j
        if a in numbers_set and b in numbers_set:
            print a, b
            difference = abs(j-i)
            if difference < answer:
                answer = difference

elapsed = time.time() - start
print 'Answer :',answer,' found in ',elapsed,' seconds!'
