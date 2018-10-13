
x = 10
z = 3
def f():
  y = 2
  x = 5
  print(x)
  print(y)
  print(z)
print("x, z, y in our f()")
f()
print("x, z, y global")
print(x)
# print(y) incorrect
print(z)