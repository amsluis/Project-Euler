'''
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''
import time
from itertools import permutations
start = time.time()

cubes = [str(x**3) for x in range(10000)]

def cube_sort(cubes):
    result = []
    for i in cubes:
        i = list(i)
        i.sort()
        i =''.join(i)
        result.append(i)
    return result

cube_sort = cube_sort(cubes)


for cube in cubes:
    sorted_cube = list(cube)
    sorted_cube.sort()
    sorted_cube = ''.join(sorted_cube)
    if cube_sort.count(sorted_cube) == 5:
        answer = cube
        break

elapsed = time.time() - start
print 'Answer :',answer,'found in',elapsed,'seconds!'
