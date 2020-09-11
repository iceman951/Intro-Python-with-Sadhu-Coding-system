number = int(input("Enter the number of rows: "))
symbol = input("Enter print symbol: ")

for i in range(number):
    for j in range(number * 2 - 1):
        if j < i or j > number * 2 - i - 2:
            print(' ', end = '')
        else:
            print(symbol, end = '')
    print()