import random
#import Day4.1(ModualExrsice)
import pi


#work with randomisiton and modual 
random_intager = random.randint(100,200)
random_float = random.random()
#this will give us a random number between 0.0000000000000 to 4.9999999999
random_float_ = random.random() * 5
try:
    #Random int number between 100 , 200
    print(random_intager)
    #here will print from anthor modual 
    print(pi.pi)
    #random float number between 0 and 1 don't include 1 
    print(random_float)
    #random float number between any two number u choose
    print(random_float_)
except Exception as e:
    raise e
# end try
