candidate = 0
answers = []

def divisible(number):
	answer = True
	for i in range(1,21):
		if number % i != 0:
			answer = False
		elif number == 0:
			answer = False
	return answer

while True:
	if candidate % 3 == 0:
		print candidate
		if divisible(candidate):
			print candidate
			break
		else:
			candidate += 2520
			print candidate
	else:
		candidate += 2520
		print candidate