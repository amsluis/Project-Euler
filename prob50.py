'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''
import time
from prime_generator import primes
start = time.time()
primes = primes(999999)
prime = set(primes)
answer = 0
longest = 0

for i in primes[0:200]:
    consec = 2
    terms = []
    flag = True
    while flag:
        index = primes.index(i)
        terms = primes[index:index+consec]
        consec_sum = sum(terms)
        if consec_sum in prime:
            if consec > longest:
                longest = consec
                answer = consec_sum
                print answer
        if consec_sum > 999999:
            flag = False
        consec += 1

elapsed = time.time() - start
print 'Answer :',answer,' found in ',elapsed,' seconds!'
