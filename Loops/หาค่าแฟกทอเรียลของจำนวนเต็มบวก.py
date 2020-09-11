def factorial(number) :
    if number == 0 : return 1
    else :
        fact = 1
        for i in range(1,number+1): 
            fact = fact * i
        return fact
number = int(input("Enter number: "))

if number < 0 : print("Cannot get",str(number) + "!")
else :
    print(str(number) + "! =", factorial(number))
