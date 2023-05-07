def is_fibonacci(num):
  a = 0
  b = 1

  while b < num:
    c = a + b
    a = b
    b = c

  if b == num or a == num:
    return True
  else:
    return False

num = int(input("Enter a number: "))

if is_fibonacci(num):
  print("True")
else:
  print("False")
