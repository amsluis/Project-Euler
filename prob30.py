import time

start = time.time()

Range = range((5*9**5))
solution_numbers = []

for i in Range:
    string = str(i)
    sum_i = 0
    for j in string:
        j = int(j)
        sum_i += (j**5)
    if int(sum_i) == i:
        solution_numbers += [i]

print solution_numbers

#need to subtract 1 as it is not a sum according to the question

answer = sum(solution_numbers) - 1
elapsed = time.time() - start

print "Answer: %d found in %d seconds." % (answer, elapsed)

