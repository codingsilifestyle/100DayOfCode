#Let's make an app to calculate the avg
Degrees = [90,99,90,75,80,75]
leng = len(Degrees)
avg = 0 
for Degree in Degrees :
    avg += Degree
print(f"Your Total Degree is {avg}") 
avg /= leng
avg = round(avg,2)
print(f"Your avarage is {avg}")