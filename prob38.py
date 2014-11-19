'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 x 1 = 192
192 x 2 = 384
192 x 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
_________
First consider the digits that need testing:
    can't be any bigger than 4 digits;
        concatenating two 5 digit numbers > 9 digits
    1 digit number can be multiplied by n~7,8, but only for 1.
        largest number is going to start with a 9, so only need to check n=5
    need to test up to:
        n = 6-len(digit)

That alone already optimizes a lot away.  Now simply brute through digits and possible strings.

Test if pandigital by getting str of correct length, then see if equiv to set of digits.
'''
import time
start = time.time()

all_digits = set(['1','2','3','4','5','6','7','8','9'])
answer = 0
for i in range(10000):
    max = 7-len(str(i))
    product = ''
    for j in range(1,max):
        product += str(i*j)
    if len(product) == 9:
        if set(list(product)) == all_digits:
            print product, i
            if product > answer:
                answer = product

elapsed = time.time() - start
print 'answer: ', answer, ' found in ', elapsed, ' seconds!'
