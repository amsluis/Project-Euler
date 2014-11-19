'''
Euler's Totient function

brute forcing isn't really an option, half a trillion calculations required

notice that more distinct prime factors = smaller totient(n)

All we really need to do is find the number below 1000000 with the most small prime factors
'''
import time
from prime_generator import primes
start = time.time()

primeList = primes(200)
limit = 1000000
answer = 1
counter = 0

while True:
    answer *= primeList[counter]
    if answer > limit:
        answer = answer / primeList[counter]
        break
    counter += 1

elapsed = time.time() - start
print 'Answer:', answer,'found in',elapsed,'seconds!'

