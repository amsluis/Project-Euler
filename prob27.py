'''
Relatively straightforward problem involving some loop control

Mostly need to loop through all possibilities of a and b, then check through each pairs resulting products.  A simple prime check will trigger the first non-prime found, returning False.  This causes the while loop in generate_products to change the loop flag to false, check if the count is a new high, and then return True if it is.  Otherwise, nothing is returned (equivalent to false).  The main loop will record the answer when passed True, otherwise it keeps searching.
'''
import time
start = time.time()
answer = 0
max_count = 0

def is_prime(number):
    prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            prime = False
    return prime

def generate_products(a,b):
    count = 1
    loop = True
    global max_count
    while loop:
        product = count**2 + a*count + b
        if is_prime(abs(product)) == False:
            loop = False
            if count > max_count:
                max_count = count
                print count
                return True
        count += 1

for a in range(-999,1000):
    for b in range(-999,1000):
        if generate_products(a,b):
            answer = a*b
elapsed = time.time() - start
print('Answer: "', answer, '" found in ', elapsed, ' seconds.')
