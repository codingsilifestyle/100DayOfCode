 #range() Funcation with looop   
for n in range(0,10,2):
     print(n)
     
#Give me the sum of even number from 1 - 100
TotalEvenNumber = 0 
for number in range(0,101):
    if((number % 2 )== 0 ):
        TotalEvenNumber += number
print(TotalEvenNumber)