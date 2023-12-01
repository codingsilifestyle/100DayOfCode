# Get The high score 
#Write a function that takes an array of scores and returns the highest score.
# If there are multiple people with the same highest score, return
Degrees = [90,99,90,75,80,75]
High = 0
for Degree in Degrees : 
    if Degree > High :
        High = Degree
print(High)
#Anthore short way and the best practice  
print(max(Degrees))