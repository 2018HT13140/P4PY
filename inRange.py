def inRange(x, y):
  return (x < 1/3 < y)
x = input("Enter integer X: ")
y= input("Enter integer Y: ")
x = int(x)
y= int(y)
print(inRange(x, y))

"""
Given an inRange(x,y) function, write a method
that determines whether a given pair (x, y) falls in the range
(x < 1/3 < y).
Essentially, you’ll be implementing the body of a function
that takes in two numbers x and y and r
eturns True if x < 1/3 < y; otherwise, it returns False.
"""
