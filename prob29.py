results = []
for i in range(2,100):
    for j in range(2,100):
        combination = i**j
        results.append(combination)
results = list(set(results))

answer = len(results)
print answer
