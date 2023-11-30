SmallPizza = 15
MediamPizza = 20
LargePizza = 25
AddPoppS = 2
AddPoppML = 3
AddChesses = 1
Bill = 0
print(f"Small Pizza: {SmallPizza}$")
print(f"Mediam Pizza: {MediamPizza}$")
print(f"Large Pizza: {LargePizza}$")
print("****************************")
print("pepporoni for small Pizza:+2$")
print("popporoni for Medium and large Pizza:+3$")
print("Extra Chesse for any size of pizza : +1$")
print("*****************************************")
ChoosePizzaSize = input("Please enter Your size of pizza(S/M/L): ")
AddPepporoni = ans = input("Do u want to add pepporoni(Y/N): ")
AddChesse = input("Do you want to add extra chess(Y/N):")
def BillCal(ChoosePizzaSize,AddPepporoni,AddChesse):
    if ChoosePizzaSize == "S":
        Bill = SmallPizza
        if AddPepporoni == "Y":
            Bill += AddPoppS
            if AddChesse == "Y":
                Bill += AddChesses
                print(f"Your Final bill is : ${Bill} ")
    elif ChoosePizzaSize == "M":
        Bill = MediamPizza
        if AddPepporoni == "Y":
            Bill += AddPoppML
            if AddChesse == "Y":
                Bill += AddChesses
                print(f"Your Final bill is : ${Bill} ")
    else:
        Bill = LargePizza
        if AddPepporoni == "Y":
            Bill += AddPoppML
            if AddChesse == "Y":
                Bill += AddChesses
                print(f"Your Final bill is : ${Bill} ")# comment: # comment: 


BillCal(ChoosePizzaSize,AddPepporoni,AddChesse)