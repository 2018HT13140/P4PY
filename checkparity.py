"""Parity is a term to express if a given integer is even or odd.
Given a checkParity(n) function, write code to determine
if a given number n is even or odd.
Think of this as a function that returns 0 if the number is even,
and 1 if it is odd.
"""

def checkParity(n):
  result = n % 2
  return result

print("Enter an integer value: ")
n=int()
result = int()
checkParity(n)
if result == 0:
  print("Even Parity")
else:
    print("Odd Parity")
