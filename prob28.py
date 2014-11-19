"""
I could make a graphical representation of the number spiral, but really I'd just be doing a bunch of work twice; getting the graphical representation is just as difficult as coming up with an algorithmic way to generate it, though more robust.
The basic strategy should be to generate the number series, enter them into an array, and sum them.
I'll do this by noticing that the jumps between numbers are regular for four steps, and then change by adding two to the interval.
"""
import time
start = time.time()

count = 0
this_number = 1
last_number = 1
interval = 2
diagonal_numbers = [1]

while interval < 1001:
    this_number = last_number + interval
    diagonal_numbers.append(this_number)
    last_number = this_number
    count += 1
    interval = 2 + 2*(count/4)
    print "this: %d, last: %d, count: %d, interval: %d" % (this_number, last_number, count, interval)

answer = sum(diagonal_numbers)
elapsed = time.time() - start
print diagonal_numbers
print "answer: %d found in %d seconds." % (answer, elapsed)

