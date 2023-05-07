"""
number = int(input("The number is: "))
factorial = 1
if number < 0:
    print("The factorial does not exist")
elif number == 0:
    factorial = 0
    print("The factorial is", factorial)
else:
    for x in range(1, number + 1):
        factorial = factorial * x

    print("The factorial is", factorial)


num = [1, 2, 3, 4, 5, 3, 1]
duplicates = []
size = len(num)
for x in range(size):
    y = x + 1
    for z in range(y, size):
        if num[x] == num[z] and num[x] not in duplicates:
            duplicates.append(num[x])

print(duplicates)
"""
"""
nums = [1, 6, 3, 2, 4, 5]
nums.sort()
median = nums[0]
if (len(nums) % 2 != 0):
    median = nums[len(nums)//2]
else:
    median1 = nums[len(nums)//2]
    median2 = nums[len(nums)//2 -1]
    median = (median1 + median2)/2

print(nums)
print("The median is", median)
"""
numbers = [1, -2, 3, -4, 5, -6, 7, 8]
positive = []
negative = []
print(numbers)
for x in numbers:
    if (x >= 0):
        positive.append(x)
    else:
        negative.append(x)

print(positive)
print(negative)