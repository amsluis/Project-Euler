'''
The nth term of the sequence of triangle numbers is given by, tn = 1/2n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''

import time
import string
start = time.time()

words = open('words.txt', 'r')
words = words.read().split(',')
triangle_numbers = set([((0.5)*x*(x+1)) for x in range(1000)])
alphabet = dict(zip(string.ascii_uppercase, range(1,27)))
answer = 0

for word in words:
    word = word.strip('"')
    total = 0
    for letter in word:
        value = alphabet[letter]
        total += value
    if total in triangle_numbers:
        answer += 1

elapsed = time.time() - start
print 'Answer :', answer, ' found in ', elapsed, ' seconds!'
