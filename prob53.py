'''
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5-C-3 = 10.

In general,


How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, are greater than one-million?
'''

import time
import math

start = time.time()
answer = 0

for n in range(1,101):
    for r in range(1, n+1):
        combination = math.factorial(n) / (math.factorial(r)*math.factorial(n-r))
        if combination > 1000000:
            answer += 1

elapsed = time.time() - start

print 'Answer :', answer, ' found in ', elapsed, ' seconds!'

