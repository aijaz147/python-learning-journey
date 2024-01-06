#1

userInput = int(input("Enter your age"))
print("Your age is:", userInput)
if (userInput >= 18):
    print("You Can Drive")
else:
    print("You Can Not Drive")

#2

bikePrice = 350000 
budget = 300000

if(budget >= bikePrice):
    print("You can buy the car")
else:
    print("You can not buy the car")

#3
    
number = -10
if(number > 0):
    print("Your Number Is Positive")
elif(number == 0):
    print("Your Number Is Zero")
else:
    print("Your Number is Negative")

# nested
    
number2 = 5

if(number2 < 0):
    print("Number is negative")
elif(number2 > 0):
    if(number2 <= 10):
        print("Number is between 1-10")
    elif(number2 >= 10 and number2 <= 20):
        print("Number is between 10-20")
    else:
        print("Number is greater then 20") 
else:
    print("Number is zero") 