'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''
import time
from itertools import permutations

start = time.time()
answer = 0

for number in range(10,999999):
    permuts = permutations(str(number))
    int_perms = []
    solution = True

    for perm in permuts:
        string = ''.join(perm)
        int_perms.append(int(string))

    for i in range(1,7):
        multiple = number * i
        if multiple in int_perms:
            pass
        else:
            solution = False
            break

    if solution == True:
        answer = number
        break

elapsed = time.time() - start

print 'Answer :', answer, ' found in ', elapsed, ' seconds!'
