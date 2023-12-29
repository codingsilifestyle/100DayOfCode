#Call a funcation to check prime number
def PrimeNumber(Num):
    is_prime = True
    for i in range(2,Num):
        if Num % i == 0:
            is_prime = False
    if is_prime :
        print("It is prime number")
    else :
        print("The Number is not prime")
        
print("**************************************")
print("     Check if the number is prime     ")
print("**************************************")
Num = int(input("Enter The Number :"))
PrimeNumber(Num=Num)