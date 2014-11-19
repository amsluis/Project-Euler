'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
'''
import time
start = time.time()

max = 0
answer = 0

for perimeter in range(1,1001):
    count = 0
    for a in range(1 , (perimeter/2) + 1):
        for b in range(1 , (perimeter/2) + 1):
            c = perimeter - a - b
            if a**2 + b**2 == c**2:
                count += 1
    print perimeter, count
    if count > max:
        max = count
        answer = perimeter

elapsed = time.time() - start
print 'Answer: ', answer, ' found in ', elapsed, ' seconds!'
