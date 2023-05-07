import random

#Choose problem that needs to be solved
problem = int(input("What problem do you want to solve (1,2,3): "))

#Problem 1
if (problem == 1):
    count = 0
    sum = 0.0 
    average = 0.0
    while True:
        number = input("Enter a number or press Enter to exit: ")
        if (number == ''):
            break

        number = float(number)
        sum += number
        count += 1

    if (count == 0):
        print("No numbers were entered!")
    else:
        average = sum/count
        print("The sum is", sum)
        print("The average is", average)

#Problem 2
elif (problem == 2):
    salary = float(input("What is the starting salary: $"))
    percentIncrease = float(input("What is the percent increase: "))
    numYears = int(input("Years teaching: "))
    print("Year\tSalary")
    for x in range(1, numYears + 1):
        print("%d\t$%.2f"%(x, salary))
        salary = salary + ((salary * percentIncrease)/100)

#Problem 3
elif (problem == 3):
    money = int(input("How much money do you want to play with: $"))
    maxMoney = money
    numRolls = 0
    sumDice = 0
    while money > 0:
        firstDice = random.randint(1, 6)
        secondDice = random.randint(1, 6)
        sumDice = firstDice + secondDice
        numRolls += 1
        if sumDice == 7:
            money += 4
        else: 
            money -= 1

        if money > maxMoney:
            maxMoney = money    

    print("The game is over after", numRolls, "rolls")
    print("The max amount of money in the pot was: $", maxMoney)