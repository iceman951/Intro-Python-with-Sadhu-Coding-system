row = int(input("Enter the number of rows: "))
symbol = input("Enter print symbol: ")
for i in range(row):
    for j in range(row * 2 - 1):
        if j < row - i - 1 or j > row + i - 1:
            print(" ", end = '')
        else:
            print(symbol, end = '')
    print()