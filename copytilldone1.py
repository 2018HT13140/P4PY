"""This program take user inputs until the user enters done.
The logic evaluates to True until the break condition 'done' is met"""
while True:
    line = input("> ")
    if line == 'done':
        break
    print(line)
print("Done!!")
