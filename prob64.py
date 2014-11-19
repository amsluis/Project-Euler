'''

'''
import time
clockStart = time.time()

answer = 0

for number in range(2,10001):

    if number ** 0.5 == int(number ** 0.5):
        continue

    start = int(number**0.5)
    a = 1
    b = int(number**0.5)


    d = (number - b**2) / a
    digit = (b+start)/d
    c = abs(b-digit*d)
    digit,a,b = digit,d,c


    check = (digit,a,b)
    count = 0
    flag = True

    while flag:
        d = (number - b**2) / a
        next_ = (b+start)/d
        c = abs(b-next_*d)

        next_,a,b = digit,d,c

        count += 1

        if (next_,a,b) == check:
            if not count % 2 == 0:
                answer += 1
            flag = False

elapsed = time.time() - clockStart
print 'Answer :',answer,'found in',elapsed,'seconds!'
