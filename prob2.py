def fib(n):
	result = []
	a,b = 0,1
	while a < n:
		result.append(a)
		a, b = b, a + b
	return result
		
	
		
def solve(number):
	total = 0
	fib_list = fib(4000000)
	for i in fib_list:
		if i % 2 == 0:
			total += i
	print total

solve(4000000)


