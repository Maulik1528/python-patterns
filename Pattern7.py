num = int(input("Enter any number:"))
for i in range(num):
    for j in range(num):
        if i == 0 or j == num -1 or i == j :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()