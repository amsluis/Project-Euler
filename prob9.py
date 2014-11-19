for a in range(1,500):
	for b in range(a,500):
		for c in range(b,500):
			if a**2 + b**2 == c**2:
				if a+b+c == 1000:
					print a*b*c
					break
