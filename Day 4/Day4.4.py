import random
#Game Let's see who will pay the play 

print("*************************************")
print("Let's see who will pay the bill today")
print("*************************************")
names = input("Enter the name of everyone and siprt the with comma ',' and space :")
NamesInArray = names.split(",")
lengths=len(names)
ran = random.randint(0,lengths - 1)
print(names[ran])


#anthor way is with random.choice()
print(random.choice(NamesInArray))