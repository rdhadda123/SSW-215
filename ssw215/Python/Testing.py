# -*- coding: utf-8 -*-
from ast import Num
from cmath import pi

"""
age = input("How old are you?")
height = input("How tall are you?")
weight = input("How much do you weigh?")
"""
"""
length = (int)(input("What is the edge length: "))
surfaceArea = 6 * length ** 2

print("The surface area is: ", surfaceArea)
"""

"""
newVideos = (int)(input("Enter number of new videos: "))
oldVideos = (int)(input("Enter number of old videos: "))
total = newVideos * 3.00 + oldVideos * 2.00
print("Total: $", total)
"""

"""
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
sum = 0
for count in range (lower, upper + 1):
    sum += count

print(sum)
"""

"""
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

a_s = a ** 2
b_s = b ** 2
c_s = c ** 2

if (a_s == (b_s + c_s) or b_s == (a_s + c_s) or c_s == (b_s + a_s)):
    print("It is a right triangle!")
elif(a_s == b_s and b_s == c_s):
    print("It is equilateral triangle!")
else:
    print("None!")
"""

"""
import random
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
"""

"""
import random
f = open("Tester.txt", 'w')
for count in range(500):
    number = random.randint(1,500)
    f.write(str(number) + "\n")


f = open("Tester.txt", 'r')
sum = 0
for line in f:
    line = line.strip()
    number = int(line)
    sum += number

print("the sum is", sum)


time_set = []
time_span = 7
for t in range(1, time_span + 1):
    time_set.append(t)
print(time_set)
print(len(time_set))


num = [1, -2, 5, 6, 0, 5, 0, 3]
result = []
print(num)
for element in num:
    if (element != 0):
        result.append(element)
        print(result)

print("Updated list is", result)
"""

data = [1, 9, 3, 4, 10, 12, 6, 5]
data.sort()
n = 3
print(data)
print("The ", n, "largest digits are: ", data[len(data) - n:len(data)])