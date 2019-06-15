num = int(input("Enter any number:"))
for i in range(num+1):
    for j in range(num - i):
        print("*",end=" ")
    print()