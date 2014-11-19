def convert_ones(number):
	key_ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	return len(key_ones[number])

def convert(number):
	length = 0
	key_teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
	key_tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
	hundreds = number / 100
	tens = number % 100
	
	if number == 1000:
		length += 11
		return length
	if hundreds:
		print 'hundreds', hundreds
		if number % 100 == 0:
			length += 7 + convert_ones(hundreds)
		else:
			length += 10 + convert_ones(hundreds)
	if (tens / 10):
		print 'tens', tens
		if tens >= 20:
			length += len(key_tens[tens / 10]) + convert_ones(tens % 10)
		elif tens >= 10:
			length += len(key_teens[tens % 10])
		else:
			length += convert_ones(tens)
	if tens < 10:
		print 'ones', tens
		length += convert_ones(tens)
	print length
	return length
	
answer = 0
for number in range(1,1001):
	print 'working on number', number
	answer += convert(number)
	print 'answer', answer
	
print answer
	