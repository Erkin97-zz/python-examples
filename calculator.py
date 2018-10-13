# calculator
# plus , minus, multiply, divide
def plus(a = 0, b = 0): # default
  return a+b

def minus(a, b):
  return a-b

def multiply(a, b):
  return a*b

def divide(a, b = 1):
  return a/b

def calculate(a, b, operation):
  if (operation == "+"):
    return plus(b = b, a = a)
  elif (operation == "-"):
    return minus(a, b)
  elif (operation == "*"):
    return multiply(a, b)
  elif (operation == "/"):
    return divide(b = b , a = a * 1.0)
  else:
    return "Incorrect operation"
    
while(True): # infinite loop, because always true    
  first = float(input("Enter first number: "))
  second = float(input("Enter second number: "))
  operation = input("Enter operation: ")
  if (operation == "end"):
    break # escape infinite loop when operation equal to end
  print("Your calculation:", calculate(first, second, operation))
print("Good bye")