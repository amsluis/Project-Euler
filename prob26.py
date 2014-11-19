'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2    =     0.5
1/3    =     0.(3)
1/4    =     0.25
1/5    =     0.2
1/6    =     0.1(6)
1/7    =     0.(142857)
1/8    =     0.125
1/9    =     0.(1)
1/10    =     0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.


strategy:
step through the division manually and calculate the remainder
if the remainder ever repeats itself, then you know you're in a repeating decimal
you then need to calculate how long the repeat is.
This is trivial for a 'simple' repeat, but more complicated for a mixed one.
'''
max_repeat = 0
for divisor in range(2,1000):
    remainder = 10
    count = 0
    remainders = []
    while remainder != 0:
        if remainder in remainders:
            if count > max_repeat:
                max_repeat = divisor
                break
            else:
                break
        remainders.append(remainder)
        if remainder >= divisor:
            remainder = remainder % divisor
        remainder *= 10
        count += 1
print 'The maximum repeat is given by 1/%d' % max_repeat
