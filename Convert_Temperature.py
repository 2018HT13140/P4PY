fahr = input('Enter Temperature in Farenheit:') #Ask user input inp
cel = input('Enter Temperature in Celius:')
try: #Adding after user input
    fahr = float(fahr) #Assign variable fahr to user input inp as float
    cel = float(cel)
    cel = (fahr - 32.0) * 5.0 / 9.0 #cel is a variable assigned to conversion formula
    print(cel)
    fahr = (cel * 9.0 / 5.0) + 32
    print(fahr)
except:
    print('Please enter a number\n')

"""This prgram is enahanced by adding try/except block to handle invalid user input"""
