list = range(1,101)

Sum = 0
SumOfSquares = 0
SquareOfSums = 0

for i in list:
	square = i**2
	SumOfSquares += square
	
for i in list:
	Sum += i
	
SquareOfSums = Sum**2

answer = SquareOfSums - SumOfSquares

print answer