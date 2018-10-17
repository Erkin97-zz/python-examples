name1 = "Erkin" # Azhar, Tima, Baktygul
name2 = "Azhar"
name3 = "Tima"
print(name3)
names = ["Erkin", "Azhar", "Tima", "Baktygul"] # list initialization
print(names[3])
names[3] = "Baktygul2" #indexing, can't index out of borders
print(names[3])

# save N number of numbers
N = int(input("Number of numbers: "))
numbers = []
print(numbers)
for i in range(N):
  numbers.append(int(input()))
  print(numbers)
print(numbers)