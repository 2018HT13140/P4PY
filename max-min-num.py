"""This program finds largest and smallest number without for loop"""
values = int()
while True:
    line = input("Enter a number : ")
    values = line
    if line == "done":
        break
#def min(values):
    smallest = None
    for value in values:
        smallest = min(values)
    print("smallest")
print("Done!!")
