a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
temp = []
 
for j in range(999999):
 
    for k in range(len(a) - 1):
        if a[k] < a[k+1]:
            largest_k = k
 
    for l in range(len(a)):
        if a[largest_k] < a[l]:
            largest_l = l
 
    temp = a[:]
    a[largest_l] = temp[largest_k]
    a[largest_k] = temp[largest_l]
    temp = a[:]
 
    for i in range((len(a)-1) - (largest_k + 1)):
        a[largest_k + 1 + i] = temp[len(a) - 1 - i]
        a[len(a) - 1 - i] = temp[largest_k + 1 + i]
 
print(a)