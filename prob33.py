'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.he fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

from fractions import Fraction
fractions = []

for numerator in range(10,100):
    for denominator in range(10,100):
        num = list(str(numerator))
        den = list(str(denominator))
        for i in num:
            if i in den and i != '0':
                num.remove(i)
                den.remove(i)
                if int(den[0]) == 0 or int(num[0]) == 0 or numerator >= denominator:
                    break
                a = Fraction(int(num[0]), int(den[0]))
                b = Fraction(numerator, denominator)
                if a == b:
                    fractions.append(b)
                    print numerator, denominator
print fractions
answer = reduce(lambda x, y: x*y, fractions, 1)
print answer.denominator
