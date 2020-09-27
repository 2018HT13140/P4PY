"""Given a string, use a findOccurence(s) function that allows you to find
the first occurrences of "b" and "ccc"​ in the string."""

"""Solution:Use find() # Use the built-in string function string.find(character)
to find the index of a specific character in a string; this returns the index of
the input character or string"""

def findOccurence(inputstr):
    a = inputstr.find(inputchar1)
    b = inputstr.find(inputchar2)
    return(a,b)

inputstr = input("Enter a string: \n")
inputchar1 = input("Enter 1st character to find: \n")
inputchar2 = input("Enter 2nd character to find: \n")

print("Outpuf of Occurances is :", findOccurence(inputstr))
