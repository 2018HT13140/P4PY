"""This program find the smallest number in the given list"""
smallest = None
print("Before the loop starts: ", smallest)
for itervar in [3,41,12,9,-1,74,15,30,100]:
    print("Number in list is: \n",itervar)
    if smallest is None or itervar < smallest:
        smallest = itervar
    print("\n Comparison in Loop : \n", itervar, smallest)
print("\n Smallest in the given list is: \n", smallest)
