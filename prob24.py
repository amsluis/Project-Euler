a = [0,1,2,3,4,5,6,7,8,9]

for permutation in range(999999):
    
    for k in range(len(a)-1):
        if a[k] < a[k + 1]:
            maxk = k

    for l in range(len(a)):
        if a[maxk] < a[l]:
            maxl = l

    #print a, maxk, maxl

    a[maxk], a[maxl] = a[maxl], a[maxk]

    for i in range(((len(a)-1) - (maxk + 1) + 1)//2):
        #print i
        a[maxk + 1 + i], a[len(a) - 1 - i] = a[len(a) - 1 - i], a[maxk + 1 + i]
		
	#print a, 'after reverse'

print(a)
