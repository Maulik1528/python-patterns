num = int(input("Enter any number:"))
k = 1
for i in range(num):
    for j in range(i+1):
        print(k, end=" ")
        k = k +1
    print()