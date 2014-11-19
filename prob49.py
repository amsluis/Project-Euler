'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''
import time
import itertools
from prime_generator import primes
start = time.time()

primes = primes(9999)
prime = set(primes)
answer = 0

for i in primes:
    if i > 999:
        permutations = itertools.permutations(str(i))
        candidate = []
        for perm in permutations:
            perm = ''.join(perm)
            perm = int(perm)
            if perm in prime:
                candidate.append(perm)
        candidate = list(set(candidate))
        candidate.sort()
        for j in candidate:
            difference = j - i
            for k in candidate[(candidate.index(j)+1):]:
                if k - j == difference:
                    answer = [str(i),str(j),str(k)]
                    print answer
                    break

answer = ''.join(answer)
elapsed = time.time() - start

print 'Answer :',answer,' found in ',elapsed,' seconds!'
