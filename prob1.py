def is_mult(number):
	if number % 5 ==0 or number %3 == 0:
		return True
	else:
		return False

def get_mult(number):
	while True:
		if is_mult(number):
			yield number
		number += 1

def solve(upto):
	total = 3
	for next_mult in get_mult(3):
		if next_mult < upto:
			total *= next_mult
		else:
			print(total)
			return
		
		
		
		
solve(100)
