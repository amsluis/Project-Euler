import itertools
permutations = itertools.permutations(range(1,10))
results = set()
for i in permutations:
    a = i[0]
    b = i[1]*1000 + i[2]*100 + i[3]*10 + i[4]
    c = i[0]*10 + i[1]
    d = i[2]*100 + i[3]*10 + i[4]
    e = i[5]*1000 + i[6]*100 + i[7]*10 + i[8]
    if a*b == e:
        results.add(e)
    if c*d == e:
        results.add(e)
    else:
        pass

answer = sum(results)
print answer
