import time
from prime_generator import primes
start = time.time()

primes = set(primes(100000))

def get_prime_factors(n):
    result = []
    for i in range(1,n/2):
        if n % i == 0:
            if i in primes:
                result.append(i)
    return result

def test_factors(factors):
    for a in factors:
        for b in factors[factors.index(a)+1:]:
            for c in factors[factors.index(b)+1:]:
                for d in factors[factors.index(c)+1:]:
                    product = a*b*c*d
                    stuff = number/product
                    if stuff in factors or stuff == 1:
                        print number,a,b,c,d
                        return True
    return False


number = 1
answer = []
while True:
    factors = get_prime_factors(number)
    if test_factors(factors):
        answer.append(number)
    else:
        answer = []
    if len(answer) == 4:
        break
    number += 1

answer = answer[0]
elapsed = time.time() - start
print 'Answer :',answer,' found in ',elapsed,' seconds!'
