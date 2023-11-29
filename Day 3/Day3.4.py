#leap year
Year = int(input("Enter the year to check if it is a leap year or not:"))
if Year % 4 == 0 :
    if Year % 100 == 0 :
          if Year % 400 == 0 :
              print("It is a leap Year")
          else:
            print("it is not a leap year")
    else:
       print("it is a leap year")
else:
    print("it isn't a leap year") 