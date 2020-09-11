row = int(input("Enter the number of rows: "))
x = -1
for i in range(row):
    for j in range(row):
        if x >= j:
            print(" ", end = '')
        else:
            print("*", end = '')
    x += 1
    print()