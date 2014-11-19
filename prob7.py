'''
def primes(n):
	sieve = [True] * (n/2)
	for i in xrange(3,int(n**0.5)+1,2):
		if sieve[i/2]:
			sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
	return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]
	
print primes(6)
'''
'''not yet complete'''

"""
def primes(n):
	#create a list of Trues half as big as n
	#these represent odd integers: 1,3,5,7,9,etc.
	#the first case of [0] is special and ignored because
	#2 is the only even prime.  This is dealt with on the return step
	sieve = [True] * (n/2)
	#now we're checking odd numbers in range 3 to sqrt(n)+1.
	#this will check all the possible odd factors for primes up to n
	for i in xrange(3,int(n**0.5)+1,2):
		#check if position at [i/2] is True.
		#if the sieve has already marked it as False, it's known not prime
		#if it is still True, then you know it's prime
		#you don't want to change the truth value,
		#but you do want to change the truth value of multiples after it
		if sieve[i/2]:
			#start setting multiples of the prime, starting at prime squared
			#I suppose you don't need to do it sooner,
			#the square is the first case of needing it.
			#a small shortcut
			
			#the complicated last term ensures you have enough Falses
			sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
	#returns the answer by converting from true values to corresponding
	#odd integer.
	return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]
	
print primes(60)
"""

def primes(n):
	sieve = [True] * (n/2)
	for i in xrange(3,int(n**0.5)+1,2):
		if sieve[i/2]:
			sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
	return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]
	
	
list = primes(1000000)
element = list[10000]
print element
	