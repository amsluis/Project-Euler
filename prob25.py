fibb = [1,1]

while len(str(fibb[-1])) < 1000:
	next_fibb = fibb[-1] + fibb[-2]
	fibb.append(next_fibb)

answer = len(fibb)
print answer
