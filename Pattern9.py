
str = 'Maulik'
n = len(str)
for i in range(n):
    for j in range(i+1):
        print(str[j], end=" ")
    print()