for row in range(6):
    for col in range(6):
        if (col == 0 or col == 5) or (row == col):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()