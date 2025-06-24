
def printBoard(grid):
    for row in grid:
        print("|",end = "")
        for number in row:
            print(number, end = "|")
        print()

def checkWinner(current_player,grid):
    for i in range(len(grid)): #This is going to pull all indices from [0,1,2]
        if grid[i][0] == grid[i][1] == grid[i][2] == current_player:
            print(f"Player {current_player} wins with a row victory")
            return True

    if grid[0][0] == grid[1][1] == grid[2][2] == current_player:
        print(f"{current_player} wins with a diagonal victory")
        return True
    
    if grid[0][2] == grid[1][1] == grid[2][0] == current_player:
        print(f"{current_player} wins with a right diagonal victory!")
        return True

    for i in range(len(grid[0])):
        if grid[0][i] == grid[1][i] == grid[2][i] == current_player:
            print(f"{current_player} wins with a column victory!")
            return True

def switchPlayer(current_player):
    if current_player == "X":
        return "O"
    if current_player == "O":
        return "X"

"""
Main functions do two things:
    1) A nice way to aggregate our program into one nice header. 
"""
def main():
    board = [
        [".",".","."],
        [".",".","."],
        [".",".","."],
    ]
    player = "O"
    check = True
    """
        1) Print board
        2) Ask for a row, column pair 
        3) Check if someone wins
        4) If no one wins, Repeat 
    """ 
    while check == True:
        print(f"{player}'s turn")
        printBoard(board)
        row = int(input("Enter the Row you want to place your piece: "))
        col = int(input("Enter the Column you want to place your piece: "))
        board[row][col] = player
        if checkWinner(player,board) == True:
            printBoard(board)
            check = False
        player = switchPlayer(player)


main()