num = int(input("Enter any number:"))
for i in range(num + 1):
    for j in range(num - i):
        print(" ",end = "");
    for j in range(i):
        print("*",end= " ")
    print()
for i in range(num):
    for j in range(i +1):
        print(" ",end = "");
    for j in range(num - i -1):
        print("*",end= " ")
    print()
