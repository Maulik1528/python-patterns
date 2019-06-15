for row in range(7):
    for col in range(5):
        if row == col or row+col == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()