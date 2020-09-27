grade = input("Enter score: ")
try:
    grade = float(grade)
    if grade < 1.0:
        if grade >= 0.9 and grade <= 1.0:
            print("A Grade!!!")
        elif grade == 0.8 or grade >= 0.7:
            print("B Grade!!")
        elif grade == 0.7 or grade >= 0.6:
            print("C Grade!")
        elif grade == 0.6:
            print("D Grade.")
        elif grade < 0.6:
            print("F Grade.")
    else:
        print("Enter Score between 0.0 and 0.9 \n")
except:
    print("Enter Score between 0.0 and 0.9 \n")
