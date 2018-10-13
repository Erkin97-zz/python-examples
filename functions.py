password = "erkin" # variable to store user password
# check password
def check_password(input_password):
  if (input_password == password): # check input and passwod
    return True # our retur value , true
  else:
    return False # false

def say_hello(): # without argument, just say hello
  print("Hello")

say_hello() # use say_hello()
# check password with function
input_password = input("Enter password: \n")
if (check_password(input_password) == True): # if our function is returning true, it means that password is true
  print("Correct password")
else:
  print("Incorrect password")


