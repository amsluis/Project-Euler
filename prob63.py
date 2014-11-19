'''
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''
import time
start = time.time()
count = 0
for i in range(1,10):
    for exponent in range(1,50):
        condition = 'no'
        number = i**exponent
        length = len(str(number))
        if exponent == length:
            condition = 'yes'
            count += 1
        # print i,'\t',exponent,length,'\t',number,'\t',condition

answer = count
elapsed = time.time() - start
print 'Answer:',answer,'found in',elapsed,'seconds!'
