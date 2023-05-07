#Rishabh Dhadda
#Midterm Exam 1

problem = int(input("What problem do you want to do: "))

if problem == 1:
    #First correct
    n = 1
    while n <= 10:
        print(n)
        n = n + 1

    #second correct
    for n in range(0,10):
        print(n+1)

    #third correct
    n = 1
    while n!= 11:
        print(n)
        print(n+1)
        n = n + 2

elif problem == 2:
    one = int(input("What is the first number: "))
    two = int(input("What is the second number: "))

    if (one > two):
        print("The larger number is", one)

    elif (one < two):
        print("The larger number is", two)

    else:
        print("The two numbers are equal")

elif problem == 3:
    for num in range(1,101):
        count = 0
        for i in range(2, num//2 + 1):
            if ((num % i) == 0):
                count = count + 1
                break
        
        if (count == 0 and num != 1):
            print(num)

elif problem == 4:
    numbers = int(input("How many numbers do you want in your list: "))
    original = []
    reverse = []

    for num in range(numbers):
        val = int(input("Number: "))
        original.append(val)

    for i in original:
        reverse = [i] + reverse #This logic adds the values from original list and then adds the empty reverse list in the beginning to push the first value to the end, so it reverses

    print(original)
    print(reverse)