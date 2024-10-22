'''
            Fizz Buzz Game Rules
Number divided by 3 called Fizz
Number divided by 5 called Buzz
Number divided by 3 and 5 called Fizzbuzz
'''

# The basic of loop to meet the condition for the FizzBuzz Game 
for num in range(1,100):
    if(num % 3 == 0 and n % 5 == 0):
        print("FizzBuzz")
    
    elif (num % 3 == 0):
        print("Fizz")
    
    elif(num % 5 == 0):
        print("Buzz")
    
    else:
        print(num)
