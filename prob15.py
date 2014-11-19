'''
Consider the diagonal from the top rigth to the bottom left of grid size n.
NB: this means n + 1 nodes along each side.
All valid paths must traverse through these nodes.
The corner nodes only have one possible path.
The next inner-most node has n possible paths to the node (draw it out).
It also has n possible paths from that node.
Going further in, you can calculate the possible paths to/from by using
	the result of previous answers.
For example: for grid size 4, the middle node is reachable from a grid size 2
Looking through these nodes, you observe a pattern of Pascal's triangle.
The paths through each node along the diagonal is given by the square of the
	elements in pascal's triangle.
Add these together for the final solution.
'''
elements = []

def pascal(n):
	elements = [1,1]
	
	while len(elements) < n:
		temp_elements = [1]
		for i in range(len(elements)-1):
			temp_elements += [int(elements[i]) + int(elements[i+1])]
			if len(temp_elements) == len(elements):
				temp_elements += [1]
				elements = temp_elements
				print elements
		if len(elements) == n:
			return elements
a = pascal(21)
print a

answer = 0
for i in a:
	answer += i**2

print answer