def greet(Name , Age , Place):
    print(f"Hi Master {Name}")
    print(f"Your Age Is {Age}")
    print(f"You study in {Place}")
    
print("******************************************")
print("            SignUp                        ")
print("******************************************")
Name = input("Enter Your Name:")
Age = input("Enter Your Age :")
Place = input("Enter the name of your Universty:")
#we use here position argument
greet(Name , Age , Place)
#And here we use Keyword 
greet(Name=Name , Age=Age,Place=Place)


