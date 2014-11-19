'''
tricky solution, depends on continued fractions to generate possible solutions to equation.

Potential solutions come from sqrt(n) continued fractions, as understood from Pell's equation solutions.  Basically you need to generate the continued fractions and plug the numerator and denominator for x and y and see if it works.  The program must generate these fractions and then test them.

Calculating continued fractions -
    sqrt(z) = sqrt(x**2 + y)
    x + y/(2x+y/(2x+y/(2x......)))
'''
import time
start = time.time()

answer = 0
largestX = 0
for D in range(2,1001):
    limit = int(D**0.5)
    if limit*limit == D:
        continue
    m = 0
    d = 1
    a = limit

    numm1 = 1
    num = a

    denm1 = 0
    den = 1

    while num*num - D*den*den != 1:
        m = d * a - m
        d = (D - m * m) / d
        a = (limit + m) / d

        numm2 = numm1
        numm1 = num
        denm2 = denm1
        denm1 = den

        num = a*numm1 + numm2
        den = a*denm1 + denm2

    if num > largestX:
        largestX = num
        answer = D

elapsed = time.time() - start
print 'Answer :',answer
print 'Largest X was',largestX
print 'Found in',elapsed,'seconds!'

