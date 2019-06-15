for row in range(7):
    for col in range(5):
        if (col == 4 and row %3 ==0) or ((col == 1 or col==2 or col==3) and row % 3 != 0 ):
            print(" ",end =" ")
        else:
            print("*",end=" ")
    print()