number = int(input("Enter the number of rows: "))
k = number-1
for i in range(0, number):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(-1, i):
        print("*", end="")
    print("")