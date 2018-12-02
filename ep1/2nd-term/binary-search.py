 # We use the binary search
# start: 0, end: len(array) - 1
# mid: start + (end - start) // 2
def search_insert(numbers, target):
  if len(numbers) == 0: # if list is empty
    return 0
  ## [start - end]
  left = 0
  right = len(numbers)
  while left != right:
    mid = (left + right) // 2
    if (numbers[mid] < target):
      left = mid + 1
    else: 
      right = mid
  return left

def my_own_sort(numbers): # sort using my own defined method
  Perfect = False # is our list perfect
  while(Perfect != True) :
    Perfect = True
    for i in range(0, len(numbers) - 1):
      if (numbers[i] > numbers[i+1]):
        Perfect = False
        numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
  return numbers

count = int(input("Enter the number of numbers: "))
num_list = [] # array list

for i in range(0, count):
  number = int(input("Enter the number: "))
  num_list.append(number) # get the number and add to list
# correct list, make it sorted and unrepeated
num_list = list(set(num_list)) # remove repeaded
num_list = my_own_sort(num_list) # sort again
# get all input and make sorted list
print("The number list is: ", num_list)

# get target number and find its position
while(True) :
  target = int(input("Enter the target number to find: "))
  result = search_insert(num_list, target)

  if result == len(num_list) or num_list[result] != target:
    print("Inserted position: ", str(result), ".", sep='')
  else:
    print("Found position: ", str(result), ".", sep='')