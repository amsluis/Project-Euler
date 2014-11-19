'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
______
Create set with primes up to 1 million (fast checking of is_prime)

Loop through range 1000000

Test if prime, and if so, test through permutations.
Permuations are generated by popping last digit and inserting to beginning
If permutations are primes and permutations are exhausted, add to list.
convert to string and test the circular rotations....
'''
from prime_generator import primes
import time
start = time.time()
circular_primes = []
primes = set(primes(1000000))
for i in range(2,1000000):
    digits = list(str(i))
    permutations = len(str(i))
    if i in primes:
        while permutations > 0:
            move_digit = digits.pop()
            digits.insert(0,move_digit)
            interger = int(reduce(lambda x,y : x+y, digits))
            permutations -= 1
            if interger in primes:
                if permutations == 0:
                    circular_primes.append(i)
                pass
            else:
                break
answer = len(circular_primes)
elapsed = time.time() - start
print 'Answer :', answer, ' found in ', elapsed, ' seconds!'
