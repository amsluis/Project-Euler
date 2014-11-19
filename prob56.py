import time
start = time.time()
answer = 0

for a in range(1,100):
    for b in range(1,100):
        digital_sum = 0
        number = a**b
        for i in str(number):
            i = int(i)
            digital_sum += i
        if digital_sum > answer:
            answer = digital_sum

elapsed = time.time() - start
print 'Answer :', answer, ' found in ', elapsed, ' seconds!'
