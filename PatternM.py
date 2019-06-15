for row in range(7):
    for col in range(7):
        if (col == 0 or col == 6) or ((col < 4) and (row == col)) or ((col > 3) and (row+col == 6)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()