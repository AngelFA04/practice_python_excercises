def create_board(n):
    """
    n: int - Lenght of the board
    """
    cube = " ---\n|   |\n ---"
    superior = "--- "
    middle = "  | "

    output = ""

    if n <= 0:
        print("You should give a number greater than 0!")
    elif n == 1:
        #print(cube)
        output = cube
    else:
        #print(" ---",superior*(n-1))
        output = " --- " + ( superior)*(n-1) + "\n"
        for i in range(n):
            #print("|",middle*(n))
            output = output + "| " + (middle)*n + "\n"
            #print(" ---",superior*(n-1))
            output = output + " --- " + (superior)*(n-1) + "\n"

    return output

if __name__ == "__main__":
    len_board = int(input("Enter the lenght of the board: "))
    print(create_board(len_board))
