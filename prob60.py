'''
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
'''

'''
Explanation:
This is some messy code, but consensus appears to be that this is the way to do it
The idea is that you pre-compute the pair concatenations and check against the precomputed sets.  You create an array as long as len(primes) so each index represents the possible pairs for that index.  Very quick check.
Then, you bluntly iterate through the possibilities, but careful use of break allows you to cut things a little shorter.  You're just checking whether a guess is possible, and if not, you break and try the next element in the loop above.  Otherwise, you check each pair to see if they're in the hash_array and only proceed if they are.
If you make it to the end of the loop, you simply check if the total is less than the current answer, and overwrite if so.
'''
import time
from itertools import combinations
from prime_generator import primes, is_prime
start = time.time()
answer = 9999999

prime_check = set(primes(99999999))
primes = primes(29999)

# hash array
hash_array = [set() for i in range(len(primes))]
for i in primes:
    a = hash_array[primes.index(i)]
    for j in range(primes.index(i) + 1, len(primes)):
        j = primes[j]
        forward = int(str(i) + str(j))
        reverse = int(str(j) + str(i))
        if forward in prime_check and reverse in prime_check:
            a.add(j)
    hash_array.append(a)

for i in range(len(primes)):
    if primes[i] * 5 >= answer:
        break
    for j in range(i + 1,len(primes)):
        if primes[i] + primes[j] * 4 >= answer:
            break
        if not primes[j] in hash_array[i]:
            continue
        for k in range(j + 1,len(primes)):
            if primes[i] + primes[j] + primes[k] * 3 >= answer:
                break
            if not (primes[k] in hash_array[i] and primes[k] in hash_array[j]):
                continue
            for l in range(k + 1,len(primes)):
                if primes[i] + primes[j] + primes[k] + primes[l]*2 >= answer:
                    break
                if not (primes[l] in hash_array[i] and primes[l] in hash_array[j] and primes[l] in hash_array[k]):
                    continue
                for m in range(l + 1,len(primes)):
                    if primes[i] + primes[j] + primes[k] + primes[l] + primes[m] >= answer:
                        break
                    if not (primes[m] in hash_array[i] and primes[m] in hash_array[j] and primes[m] in hash_array[k] and primes[m] in hash_array[l]):
                        continue
                    total = sum([primes[x] for x in [i,j,k,l,m]])
                    if answer > total:
                        answer = total
                        print total,i,j,k,l,m

elapsed = time.time() - start
print 'Answer :',answer,' found in ',elapsed,' seconds!'
