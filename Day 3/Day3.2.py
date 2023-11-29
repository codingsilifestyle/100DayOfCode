#Second Example Nested it example in buy a ticket
Hight = int(input("Enter your Hight:"))

if Hight >= 150 :
    Age = int(input("Enter your Age:"))
    if (Age >= 18 and Age <= 35):
        print("You can buy the ticket")
    else:
        print("You can't buy the ticket you are under 18 ")
        # comment: 
else:
    print("You can't buy the ticket sorry you hight under the required !")
    