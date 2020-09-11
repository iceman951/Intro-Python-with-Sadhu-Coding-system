number = int(input("Enter number: "))
decNumber = number
binNumber = ""
while decNumber != 0 :
    remainder = decNumber % 2
    decNumber = decNumber // 2
    binNumber = str(remainder) + binNumber
print(number,"is", binNumber, "in base 2.")
