file = open("Exam file_1.txt", "r")
contents = file.read()
file.close()

lines = contents.split("\n")

mylist = []

for line in lines:
  mylist.append(int(line))

print(mylist)

def median_fun(mylist):
  mylist.sort()
  length = len(mylist)

  if length % 2 == 1:
    return mylist[length // 2]

  else:
    return (mylist[length // 2] + mylist[length // 2 - 1]) / 2

def mean_fun(mylist):
  sum = 0
  for num in mylist:
    sum += num

  return sum / len(mylist)

print("The median is: ", median_fun(mylist))
print("The mean is: ", mean_fun(mylist))