num = int(input("Enter any number:"))
for row in range(num + 1):
    for column in range(row):
        if row % 2 != 0 :
            print("*", end=" ")
    print()