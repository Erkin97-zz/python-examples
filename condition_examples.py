# check if input number is even or odd
our_input_number = int(input("Enter even number:\n"))
mod_to_2 = our_input_number % 2 # ostatok ot 2
if (mod_to_2 == 0):
  print("It's even bro") #code block
  print("good job")
else:
  print("It's odd number stupid")

# check if input number is even and greater than 100 but less than 1000
# mod
# > 100
# < 1000
# test and
if (our_input_number % 2 == 0 and our_input_number >= 100 and our_input_number < 1000):
  print("Correct")
else:
  print("incorrect")

#test or
if (our_input_number % 2 == 0 or our_input_number >= 100):
  print("Correct")
else:
  print("incorrect")

# compare strings
# check if password is correctt
password = "pass1"
input_password = input("Enter password: \n")
if (input_password == password):
  print("Welcome home")
else:
  print("Incorrect password")
