'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
import itertools
import time
start = time.time()

def is_prime(n):
    for i in range(2,(int(n**0.5)+1)):
        if n % i == 0:
            return False
            break
    return True

pandigital = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
answer = 0
flag = True

while flag:
    for i in range(9876543,0,-1):
        digits = set(list(str(i)))
        if len(digits) == 7:
            if '0' in digits:
                pass
            elif '9' in digits:
                pass
            elif '8' in digits:
                pass
            else:
                if is_prime(i):
                    print i
                    answer = i
                    flag = False
                    break

elapsed = time.time() - start
print 'Answer :', answer, ' found in ', elapsed, ' seconds!'
