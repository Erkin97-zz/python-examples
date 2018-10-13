
# math functions user defined functions
# square
import math


def square(x = 5): # take x and return x^2
  return x*x

print("Square:", square())

our_number = int(input("Enter number: "))

print("Square:", square(our_number))


print("minimum", min(5, 6, 2, 3)) # pre-defined, python already implemented for us

# library
print("cosinus",  math.cos(our_number)) #library defined function

#keyword arguments
def power(base, exponent):
  return base ** exponent
print(power(10, 2))
print(power(base=2, exponent=10))
print(power(exponent=10, base=2))

#keyword arguments of print
