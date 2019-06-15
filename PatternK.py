for row in range(7):
    for col in range(5):
        if (col == 0) or (col > 0 and row+col == 4 ) or (col > 0 and row-col == 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()