# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """


# @author: Nafiseh
# """

# # ----------------------------
# def square_1 (x):
#     y = x * x
#     return y

# print (square_1 (7))

# # ---------------------------

# def average (mylist):
#     theSum = 0
#     for i in mylist:
#         theSum += i
#         Ave = theSum / float (len (mylist))
        
#     return Ave    

# print (average ([1,3,5,7]))

# # --------------------------

# def summation (lower, upper):
#     result = 0
#     while lower <= upper:
#         result +=lower
#         lower += 1
#     return result    


# print (summation (1, 4))
# print (summation (50, 100))

# --------------------------

# def main ():
#     number = int (input ("Enter a number: "))
#     result = square_2 (number)
#     print ("The square of", number, "is", result)
    
# def square_2 (x):
#     return x * x


# main ()     


# # -------------------------
# def displayRange (lower, upper): # displayRange function outputs the numbers from lower through upper
#     while lower <= upper:
#         print (lower)
#         lower = lower +1
# displayRange(2, 5)

def displayRange (lower, upper): # Converting displayRange function to a recursive function
    if lower <= upper:
        print (lower)
        displayRange (lower +1, upper)

displayRange(2, 5)

def summation (lower, upper):   # recursive version of summation function
    if lower > upper :
        return 0
    else:
        return lower + summation (lower +1, upper)

print (summation (4,9))
# # -----------------------------

# #def runForeever (n):   # infinite recursion 
# #    if n > 0:
# #        runForeever (n)
# #    else:
# #        runForeever (n-1)
# #print (runForeever (1))        

# import math 
# f = abs
# print (f (-4))

# funcs = [abs, math.sqrt]
# print (funcs [0](-5)) # apply abs to -5
# print (funcs [1](2))  # apply math.sqrt to 2

# # ------------------------

# words = ["231", "20", "-45", "99"]
# map (int, words)
# print (words)

# words = list (map (int, words))
# print (words)

# # ------------------------
# double = lambda x: x * 2 
# print (double (5))

# def double (x):
#     return x * 2

# print (double (5))

# # -----------------------
# x = lambda a, b, c : a + b + c

# print (x (5, 6, 2))

def fact(num):
    if num == 1:
        return num
    else:
        return num * fact(num - 1)



number = int(input("Enter number: "))
print(fact(number))