#BMI calculater it doesn't work hahahaha
print("Welcome to BMI calculater 2.0 ")
print("******************************")
hight = float(input("Enter Your Hight:"))
wight = float(input("Enter your wight:"))
BMI = round(wight / hight**2)
if BMI < 18.5 :
    print(f"Your BMI is {BMI} And you are underwight")
elif BMI > 18.5 and BMI < 25 :
    print(f"Your BMI is {BMI} And you are normal wight")
else:
    print(f"Your BMI is {BMI} And you are clinically obese")
    
