# example of while
# decrease any input until 0
input_number = int(input("Enter your number: ")) # get number from input
while(input_number > 0):
  print(input_number, end=" ") # end by default will go to next line, but we did it to put space
  input_number = input_number - 1 #decrease by one
print("\nGood bye")