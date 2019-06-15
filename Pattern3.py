num = int(input("Enter any number:"))
for row in range(num):
    for j in range(num - row - 1):
        print(end = " ")
    for j in range(row + 1):
        print("*",end = " ")
    print()