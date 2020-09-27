"""Given a getStr() function, write the necessary sequence of
operations to transform the string (containing three literals)
in such a way that every literal is tripled​ respectively"""

def getStr(s):
  s=s[:1] + s[0] + s[1:]# Transform the string
  s=s[:1] + s[0] + s[1:]
  s=s[:3] + s[3] + s[3:]
  s=s[:3] + s[3] + s[3:]
  s=s[:6] + s[6] + s[6:]
  s=s[:6] + s[6] + s[6:]
  # Update the length of string
  strlen = len(s)
  return [s, strlen]

inputstr = input("Enter a string: \n")
print("Output is: ", getStr(inputstr))

"""
Solution: Use len() and concatenation(+) Operation #
Use len(str) to calculate the length of string str

Concatenate value at a certain position in the string using
the concatenation operation

Given a string 'str', use the following piece of code to
transform the string

str = str[:position] + character_to_insert + str[position:]

The character needs to be inserted where the position is in the code.
"""
