import time
start = time.time()

# Make alphabet dictionary to convert letters to numbers

alphabet = ['','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a = list(enumerate(alphabet))
key = {}
for (i,j) in a:
	key[j] = i
	
# Open file
	
names = open('names.txt', 'r')
names = names.read()
names = [name.strip('"') for name in names.split(",")]
names.sort()

# Simple function to convert a word to the sum of the numerical conversion

def make_numerical(word):
	sum = 0
	word = word.lower()
	for letter in str(word):
		sum += key[letter]
	return sum
	
# Loop to build the sum
	
answer = 0
incriment = 1
for name in names:
	answer += make_numerical(name) * incriment
	incriment += 1
	
elapsed = time.time() - start
print '\nSum:',answer,'\nAnswer found in: ', elapsed, '\n'
