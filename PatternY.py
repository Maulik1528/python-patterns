for row in range(7):
    for col in range(6):
        if ((row == col) and col < 3) or ((row + col == 4 and col > 2)) or ((col == 2) and (row > 1 and row < 6)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()