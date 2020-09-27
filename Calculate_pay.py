hrs = input("Enter Hours Worked: \n")
rate = input("Enter Hourly Rate: \n")
try:
    hrs = float(hrs)
    rate = float(rate)
    pay = float()
    if hrs > 40:
        new_rate = rate * 1.5 #if number of hours is greater than 40
        pay = hrs * new_rate
    else:
        pay = hrs * rate
    print("Payment calculated is: ")
    print(pay)
except:
    print("Enter a numeric value.")
