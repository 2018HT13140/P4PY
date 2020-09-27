"""Given an inRange(x,y) function, write a method that determines whether a given pair (x, y) falls in the range (x < 1/3 < y).
Essentially, you’ll be implementing the body of a function that takes in two numbers x and y and returns True if x < 1/3 < y;
otherwise, it returns False."""

def inRange(x, y):
  return (x < 1/3 < y)

x = int()
y = int()
print("Enter an integer value for x: ")
print("Enter an integer value for y: ")
print(inRange(x,y))
print("True")
print(inRange(x,y))
print("False")

"""Relational operators such as < return either True or False and the solution,
therefore, becomes extremely straightforward.
We can simply return whatever the x < 1/3 < y statement yields"""
