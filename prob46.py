'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2x12
15 = 7 + 2x22
21 = 3 + 2x32
25 = 7 + 2x32
27 = 19 + 2x22
33 = 31 + 2x12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''
import time
from prime_generator import primes
start = time.time()

primes = primes(10000)
prime_set = set(primes)
answer = 0

for number in range(3,10000,2):
    if not number in prime_set:
        is_Goldbach = False
        for i in range(1,int(number**0.5)):
            remainder = number - 2*(i**2)
            if remainder in prime_set:
                is_Goldbach = True
        if is_Goldbach == False:
            print number
            answer = number
            break

elapsed = time.time() - start
print 'Answer :',answer,' found in ',elapsed,' seconds!'
