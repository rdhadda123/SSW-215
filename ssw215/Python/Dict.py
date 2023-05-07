myDict = {"A": 2, "B": 4, "C": 6}
result = 1
for key in myDict:
    result = result * myDict[key]

print(result)

letters = "abcabcdefghi"
frequencies = {}
for c in letters:
    frequencies[c] = frequencies.get(c, 0) + 1

for f in frequencies.items():
    print(f)

myDict = {"A": 2, "B": 4, "C": 6}
result = 0
for key in myDict:
    result = result + myDict[key]

print(result)

myDict = {"A": 2, "B": 4, "C": 6, "D" : 8}
myDict2 = {"A": 4, "B": 6, "C": 8}
common = {}

for x in myDict.keys():
    for y in myDict2.keys():
        if x == y:
            common[x] = myDict[x] + myDict2[y]

print(common)


myDict = {"A": 2, "B": 4, "C": 6, "D" : 8}
print(max(myDict.items()))
print(min(myDict.items()))

import random

data = {}

for i in range(3):
    salary = random.randint(10000, 1000000)
    name = input("What is employee name: ")
    data[name] = salary

print(data)

