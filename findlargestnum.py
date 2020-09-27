"""This program find the largest number in the given list"""
largest = None
print("Before the loop starts: ", largest)
for itervar in [3,41,12,9,74,15,30,100]:
    print("Number in list is: \n",itervar)
    if largest is None or itervar > largest:
        largest = itervar
    print("\n Comparison in Loop : \n", itervar, largest)
print("\n Largest in the given list is: \n", largest)
