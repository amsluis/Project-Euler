'''
Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) numbers and are generated by the following formulae:

The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.

The set is cyclic, in that the last two digits of each number is the first two digits of the next number (including the last number with the first).
Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882), is represented by a different number in the set.
This is the only set of 4-digit numbers with this property.
Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.
'''
import time
start = time.time()
numbers = {}

def Triangle():
    n = 1
    number = None
    while len(str(number)) < 5:
        number = n*(n+1)/2
        if len(str(number)) == 4:
            numbers[str(number)] = 'Tri'
        n += 1
def Square():
    n = 1
    number = None
    while len(str(number)) < 5:
        number = n**2
        if len(str(number)) == 4:
            numbers[str(number)] = 'Square'
        n += 1
    return numbers

def Pentagonal():
    n = 1
    number = None
    while len(str(number)) < 5:
        number = n*(3*n-1)/2
        if len(str(number)) == 4:
            numbers[str(number)] = 'Pent'
        n += 1
    return numbers

def Hexagonal():
    n = 1
    number = None
    while len(str(number)) < 5:
        number = n*(2*n-1)
        if len(str(number)) == 4:
            numbers[str(number)] = 'Hex'
        n += 1
    return numbers

def Heptagonal():
    n = 1
    number = None
    while len(str(number)) < 5:
        number = n*(5*n-3)/2
        if len(str(number)) == 4:
            numbers[str(number)] = 'Hept'
        n += 1
    return numbers

def Octagonal():
    n = 1
    number = None
    while len(str(number)) < 5:
        number = n*(3*n-2)
        if len(str(number)) == 4:
            numbers[str(number)] = 'Oct'
        n += 1
    return numbers

Triangle()
Square()
Pentagonal()
Hexagonal()
Heptagonal()
Octagonal()

master_list = ['Tri', 'Square', 'Pent', 'Hex', 'Hept', 'Oct']
for i in numbers:
    master_list_1 = list(master_list)
    master_list_1.remove(numbers[i])
    last_digits = i[2:]
    for j in numbers:
        if not (numbers[j] in master_list_1 and i[2:] == j[:2]):
            continue
        master_list_2 = list(master_list_1)
        master_list_2.remove(numbers[j])
        for k in numbers:
            if not (numbers[k] in master_list_2 and j[2:] == k[:2]):
                continue
            master_list_3 = list(master_list_2)
            master_list_3.remove(numbers[k])
            for l in numbers:
                if not (numbers[l] in master_list_3 and k[2:] == l[:2]):
                    continue
                master_list_4 = list(master_list_3)
                master_list_4.remove(numbers[l])
                for m in numbers:
                    if not (numbers[m] in master_list_4 and l[2:] == m[:2]):
                        continue
                    master_list_5 = list(master_list_4)
                    master_list_5.remove(numbers[m])
                    for n in numbers:
                        if not (numbers[n] in master_list_5 and m[2:] == n[:2]):
                            continue
                        if i[:2] == n[2:]:
                            answer = [i,j,k,l,m,n]

print answer
stuff = []
for i in answer:
    stuff.append(int(i))
answer = sum(stuff)

elapsed = time.time() - start
print 'Answer :',answer,'found in',elapsed,'seconds!'
