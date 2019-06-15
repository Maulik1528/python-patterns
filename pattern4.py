num = int(input("Enter any number:"))
for i in range(1, num+1):
    for j in range(1, i):
        print(end=" ")
    for j in range(num - i):
        print("*", end=" ")
    print()