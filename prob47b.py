import time
from prime_generator import primes
start = time.time()

primes = set(primes(100000))

def get_prime_factors(n):
    result = []
    for i in range(1,int(n**0.6)):
        if n % i == 0:
            if i in primes:
                result.append(i)
    return result

target = 4
number = 1
answer = []
while True:
    factors = get_prime_factors(number)
    if len(factors) >= target:
        answer.append(number)
        #print number, factors
    else:
        answer = []
    if len(answer) == 4:
        break
    number += 1

answer = answer[0]
elapsed = time.time() - start
print 'Answer :',answer,' found in ',elapsed,' seconds!'
