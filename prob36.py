'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''
import time
start = time.time()

answers = []
for i in range(1000000):
    base_ten = str(i)
    base_ten_reverse = str(i)[::-1]
    base_two = str(bin(i)[2:])
    base_two_reverse = str(base_two)[::-1]
    if base_ten == base_ten_reverse and base_two == base_two_reverse:
        answers.append(i)

answer = sum(answers)
elapsed = time.time() - start
print'Answer :', answer,' found in ', elapsed,' seconds.'
