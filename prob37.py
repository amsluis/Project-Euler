'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''
import time
from prime_generator import primes
start = time.time()
primes = set(primes(1000000))
not_primes = set(range(1000001)) - primes
answers = []

for prime in primes:
    flag = True
    length = len(str(prime))
    if prime < 10:
        flag = False
    for i in range(length):
        a = int(str(prime)[i:])
        b = int(str(prime)[:(i+1)])
        if a in not_primes:
            flag = False
        if b in not_primes:
            flag = False
    if flag:
        print prime
        answers.append(prime)

answer = sum(answers)
elapsed = time.time() - start
print'Answer :', answer,' found in ', elapsed,' seconds.'
