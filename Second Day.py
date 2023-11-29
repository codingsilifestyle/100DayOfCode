#Second Day project 
#Daytwo_out_of = 100 Of code 
print("Welcome to the tip calculter")
TotalBill = float(input("What was the Bill:$"))
Precent = float(input("What is the precent that u want to take?10,12,15:"))
People = float(input("How many people to split the bill: "))
Precent /= 100 
Precent += 1
TotalBill = round((TotalBill / People) * Precent,2)

print(f"Each person should give:{TotalBill}")


