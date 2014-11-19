total = 0

for i in range(1,1000):
    i = str(i**i)
    last_digits = int(i[-10:])
    total += last_digits

total = str(total)
print total[-10:]
