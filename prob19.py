Days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
Months = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def February(year):
	if year % 100:
		if year % 400:
			return 29
		else:
			return 28
	elif year % 4:
		return 29
	else:
		return 28
	
day = 0	
month = 0
year = 1901
Sunday_1sts = 0
while year < 2001:
	print 'Year: ',year,' Month: ', Months[month % 12],' Days: ',day, ' Answer: ', Sunday_1sts
	if (day ) % 7 == 6:
		Sunday_1sts += 1
	day += Months[month % 12]
	if month % 12 == 1:
		day += February(year)
	month += 1
	if month % 12 == 0:
		year += 1
		
print 'Final answer is: %s' % Sunday_1sts
	
	