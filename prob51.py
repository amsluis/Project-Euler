'''
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
'''
import time
from prime_generator import primes

start = time.time()
primes = set(primes(999999))
answer = []
flag = True

def getReplacements(number):
    number = str(number)
    for i in range(len(number)):
        for j in range(len(number)):
            for k in range(len(number)):
                if i < j < k:
                    result = []
                    for digit in range(1, 10):
                        digit = str(digit)
                        replaced = number[:i] + digit + number[(i+1):j] + digit + number[(j+1):k] + digit + number[(k+1):]
                        if int(replaced) in primes:
                            result.append(replaced)
                        if len(result) == 8:
                            return result

while flag:
    for i in range(99999,999999):
        answer = getReplacements(i)
        if answer:
            length = len(answer)
            if length == 8:
                flag = False
                break

elapsed = time.time() - start

print 'Answer : ', answer[0], ' found in ', elapsed, ' seconds!'

