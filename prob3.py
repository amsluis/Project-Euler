number = 600851475143
answer = 0

def primes(n):
	sieve = [True] * (n/2)
	for i in xrange(3,int(n**0.5)+1,2):
		if sieve[i/2]:
			sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
	return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

prime_list = primes(int(number**.5))	
#print prime_list

for i in prime_list:
	if number % i == 0:
		answer = i
		
print answer
		
















