import time
start = time.time()

guess = 1000000
triangle = []
pentagonal = []
hexagonal = []
for i in range(2,guess):
    T = i*(i+1)/2
    P = i*(3*i-1)/2
    H = i*(2*i-1)
    triangle.append(T)
    pentagonal.append(P)
    hexagonal.append(H)

pentagonal = set(pentagonal)
hexagonal = set(hexagonal)

for number in triangle:
    if number in pentagonal:
        if number in hexagonal:
            if number > 40755:
                answer = number
                break

elapsed = time.time() - start
print 'Answer :',answer,' found in ',elapsed,' seconds!'
