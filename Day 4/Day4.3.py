# List of things or Array 
#Array start from index 0
Array = ["Mohammed","Ali","Qasm"]
#Add a anthor thing to the end of the array
Array.append("item")
print(Array[3])
#loop to print the array
for ary in Array :
    print(ary)
#multidamnition array 
Array2 = [["Mohammed",22,777800000],["Ali",30,771234567]]
#loop for multi array
for r in Array2 :
    for c in r :
        print(c , end=" ")
    print()

