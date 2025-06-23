board = [
    ["X",".","."],
    [".","X","."],
    [".",".","X"],
]

for row in board:
    print("|",end = "")
    for number in row:
        print(number, end = "|")
    print()

""" 
We're gonna check for rows and left diagonal

and for the rest of class you're going to try and implement columns and a right diagonal

X
 X          <= This is a left diagonal 
  X

  X
 X         <= This is a right diagonal
X

Right now all we're doing is checking for a winner, tomorrow we're going to implement the actual game
"""

"""
Row victories are pretty easy 

[., ., .] #Row 0 board[0][0-2] 
[., ., .] #Row 1
[., ., .] #Row 2

We want to check if all of the elements in a row are identical.

That indices will make this entire problem way easier for-(i,j) loops are key 

if board[0][0] == board[0][1] == board[0][2] == current_player <= This is a top row victory 
"""

current_player = "X" #you can make this O if you want but for the sake of the example we're going to use X

#row victory
for i in range(len(board)): #This is going to pull all indices from [0,1,2]
    if board[i][0] == board[i][1] == board[i][2] == current_player:
        print(f"Player {current_player} wins with a row victory")


#Left Diagonal Victory 
""" 
  [0][0]
    X 0 0
    0 X 0 What is the middle index? [1][1]
    0 0 X [2][2]
"""
if board[0][0] == board[1][1] == board[2][2] == current_player:
    print(f"{current_player} wins with a diagonal victory")

#Right Diagonal Victory 
""" 
            [0][2]
        0 0 X
        0 X 0 What is the middle index? [1][1]
[2][0] X 0 0 

TODO: 
Figure out what the if-statement has to be for a right diagonal victory and check to see if it works 
"""


#Column Victories 
"""
 0 1 2
[.,.,X] #Row 0
[.,.,X] #Row 1
[.,.,X] #Row 2

TODO: 
So we still need a for loop, can you adapt the way we won with a row victory to a column victory? 
"""