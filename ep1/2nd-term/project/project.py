# get user command
def get_command() :
  command = input("Enter command (i or s or t or e): ")
  return command
# implement i command, to get length of sticks
stick_lengths = []
def do_i_command():
  number_of_stick = int(input("Enter the number of sticks: "))
  global stick_lengths # list of stick lengths
  input_values = []
  for i in range(number_of_stick):
    length = int(input("Enter the length of stick: "))
    stick_lengths.append(length)
    input_values.append(length)
  print(input_values)
# find two pairs with sum of target
def do_s_command():
  target = int(input("Enter the target number: "))
  # a + b == target return
  global stick_lengths
  for a in range(len(stick_lengths)):
    for b in range(len(stick_lengths)):
      if (a == b):
        continue
      if (stick_lengths[a] + stick_lengths[b] == target):
        print([a, b])
        return # exit funtion
  print("Cannot find!")
# loop commands
while(True):
  command = get_command()
  if (command == "i"):
    do_i_command()
  elif (command == "s") :
    do_s_command()
  elif (command == "e"):
    break
  else:
    print("Wrong commands ... i or s or t or e!")
# finish
print("Good bye!")