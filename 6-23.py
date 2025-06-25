"""
PSET 2 was posted saturday afternoonish. That's due today at 11:59 PM <= Remind for questions on this at the end of class

For the plan this week:
    - Cover Nested For loops
    - Cover 2D Lists
    - Cover Dictionaries
    - Cover User Made Functions <= The end of the python unit 

We should start thinking about a final python project: 
    - Extremely open ended OR 
    - "Look at some sample runs, try and copy the program" 

    - A Student Directory, A bank program, choose your own adventure text-based game. <= With this in mind, you should start thinking
    about what you would want to do.

    - If this is going to be due on Friday 6/27 (I'm probably going to be pretty flexible on this one), 
    I'd probably want some sort of proposal by Tomorrow at 11:59 PM (with the PSET 3) 
    if there is one

    - I'll also post a design specsheet that should cover the rubric. 

    - I probably won't do anything instructional on Thursday and reserve that 4-hour timeslot with last minute questions/help for your
    final python assignment 
"""

"""
Last Class we covered a lot: We covered looping statements and lists and how to manipulate them. Basically today we're going to 
touch on more advanced ways of doing both of these tasks. 

    - Nested For-loops
    - 2D Lists
    - Dictionaries
"""

#for i in range(10):
    #print(i)

"""
Refresher: What a for-loop does is create a temp variable that iterates over some "list-like" object 
    - an actual list
    - a range of numbers

if it's an actual list we called a for-each loop, if it's a range of numbers we called a for-i loop. The question we want to answer is:

What happens if we put another for-loop inside this current for-loop 
"""

for i in range(4):
    for j in range(4):
        print(f"outer loop {i}, inner loop {j}")

"""
So the outer-loop does not go to the next iteration until the inner-loop is completely done and exits the loop. 

If you were counting with your two hands:

Left hand was multiples of 5 and your right hand was single 1's 

-nothing on your left hand
    - count up to five on your right hand
-one on your left hand
    - count up to five on your right hand
.
.
.
-five on your left hand
    -five on your right hand 

Why is something like this useful? Let's try printing a multiplication table for 1-12.

What the print statement does: it implicitly adds a new-line at the end of your statement.

print(1) <= actually really prints "1\n" 

print() also accepts a second parameter called "end"
"""
for i in range(1,13):
    for j in range(1,13): #Your inner loop has to be of a different variable name
        print(i * j, end = " ")
    print() #This print statement is actually "\n"
    
""" 
Make sure your empty print() is in the correct for-loop. Let's do a non math example that's also a non range example

Scenario: I'm running america's greatest restaurant Olive Garden 
    -Two lists
        - Entrees 
        - Sides
"""

entrees = ["Steak","Pasta","Roasted Chicken","Grilled Shrimp"]
sides = ["Fries","Breadsticks","Side Salad"]

""" 
Every entree can have one side. So let's print all of the possible combinations of entrees and sides
"""
print("Welcome to olive garden")
for dish in entrees:
    for side in sides:
        print(f"Main Dish: {dish}, Side: {side}")

""" 
for <variable> in <list>;

variable can be any name you want it to be: 

<list> has to exist beforehand or you make it inside the in statement 
"""

"""
*
* *
* * *
* * * *
* * * * *

Printing something like this is the ultimate "Intro to CS" HW problem.

  *
 * *
* * *

^ This one also shows up. In principle: The left hand pyramid is not too dissimilar to the times-table 
"""

""" 
Range(n) specifically returns a list of numbers from [0,n-1]
range(start,end) returns a list of numbers from [start,end-1]
"""
""" 
    We know that i will vary from 1-5
    
    On the first run, it's going to be 
        i = 1
    Second run,
        i = 2
    
"""

"""
        if it's 0-6 

        i = 1 
        j = 1 range(1)
            [0] = happens once

        i = 2
        j = 2 range(2)
            [0,1] = inner loop happens twice


        i = 3
        j = 3 range(3)
            [0,1,2] = happen 3 times
"""
for i in range(1,6):
    for j in range(i):
        print("*", end = " ")
    print()

""" 
Do we think we could implement the right handed one? 

        *
      * *
    * * *
  * * * *

I think I'll leave this as a challenge problem for a potential PSET 3 that might get released at 5pm today. 

15 Minute break until 9

I just covered nested for-loops in about 45 minutes. A big motivator for why we did nested for-loops is because it allows us 
to have a natural way of traversing 2D-lists

2D-lists sound incredibly freightening at first.

2D list: a list that contains lists as its elements 

A list: an ordered list of elements
A 2D list is just a list where the elements are also lists. 
"""

twodlist = [
    [1,2,3,4], #Row 0
    [5,6,7,8], #Row 1
    [9,10,11,12], #Row 2
    [13,14,15,16] #Row 3
            ] #New line for each individual list is a common convention 
print(twodlist)
#Which coordinate corresponds to the value "2"?
""" 
There are question's we need to know the answer to:

1) how do we access elements in our 2D list
2) How do we add new lists to our 2D List
3) How do we add new elements to each sublist 

"""

mylist = [1,2,3,4]
#Remember that lists are ordered by indices 0 - length-1
print(mylist[1])

""" 
all we really need to do to get an element out of a 2D list is by using two square brackets next to each other. There's some nuance
to this:

    - We want to think of 2D lists as either a grid or a spreadsheet. In cartesian Coordinates, the point (0,0) is the center

    - but in a 2D list, (0,0) is actually the top left corner 
    "2D Lists expand to the Down and Right" 

    - Best not think of indices as (x,y) coordinates, but think of them as (row,column) pairs 

"""
twodlist = [
    [1,2,3,4], #Row 0
    [5,6,7,8], #Row 1
    [9,10,11,12], #Row 2
    [13,14,15,16] #Row 3
            ] #New line for each individual list is a common convention 
print(twodlist)
#Which coordinate corresponds to the value "2"?
print(twodlist[0][1])
#Syntax is <nameoflist>[row][column]
#NOT <nameoflist>[row,column] NOT <name of list>(row)(column)

"""
We can pull individual elements out of our 2D list. What about individual rows? <= This behaves exactly how a regular list would 
"""
print(twodlist[0])
print(twodlist[1])
""" 
We know how to access individual rows and individual elements. 

How do we add a row to a 2D list? 

"""
twodlist.append([17,18,19,20])
print(twodlist)

"""
Follow up question: How do we add to an individual row? 

Syntax: <name of the list>[<number of row that we want to add to>].append(item)


Now I want to travese our 2D list, convieniently we just learned about nested for-loops. 

for-each loop first
"""

"""
Following a piece of code on a piece of paper is called a stack trace

for row in twodlist
row = twodlist[0] ([1,2,3,4])
    for item in row 
        item = 1
        do thing
        item 2
        do thing again
        .
        .
        .
        item = 4
row = twodlist[1] ([5,6,7,8])
        for item in row 
        item = 5
        do thing
        item 6
        do thing again
        .
        .
        .
        item = 8
"""

#For each example
print("For Each")
for row in twodlist:
    for item in row:
        print(item) 

#For-i,j 


print("For i,j")
for i in range(len(twodlist)): #range = [0,1,2,3]
    for j in range(len(twodlist[0])): #what goes inside len()?
                                      #Right now it doesn't matter what index I put inside of len(twodlist[])
        print(twodlist[i][j])

"""

twodlist[0].append(10)
twodlist = [
    [1,2,3,4,10], #Row 0
    [5,6,7,8]#??? at index 4 which doesn't exist, #Row 1
    [9,10,11,12], #Row 2
    [13,14,15,16] #Row 3
            ]

            This is the pitfall for doing for-i,j loops over 2d-lists, you need to be careful with the sizes of the individual rows

            
            This is a big problem for when you edit lists mid-loop 
"""

twodlist = [
        [1,2]#100 Now these rows are different sizes 
        ,[3,4]
]
"""
for i in range(len(twodlist)):
    for j in range(len(twodlist[0])):
        if twodlist[i][j] == 2:
            twodlist[0].append(100)
        print(twodlist[i][j])

"""        

""" 
Stack Trace

first outer-loop
i = 0
inner loop (conditional on the size of the first row)
    j = 0
    if list[0][0] == 2:
        FAIL
    print(thing)
    j = 1
    if list[0][1] == 2: TRUE
        append 100 to the first row 

second outer-loop
i = 1
inner loop
    j = 0
    if list[1][0] == 2:
        FAIL
    j = 1
    if list[1][1] == 2:
        FAIL
    if list[1][2] == 2:
        FAIL 
        it's going to catastrophically fail because there is no list[1][2]

The point of demonstrating this stack trace is you need to be extremely careful with the size of your rows when manipulating a 2D list
"""

""" 
To fix this I would probably use a while loop as the inner loop

Recall the difference between these two kinds of loops:

for loops: iterate over a list of things (objects in a list or a range of numbers)

while loops: repeat until some exit condition is met (this is some boolean sentence )
"""

"""
To translate a for-i loop into a while loop, you need to have some counting variable that counts up to the length of some list

"""
print("Fixed example")
for i in range(len(twodlist)): #Indices of all of the rows
    j = 0
    while j < len(twodlist[i]): #do we know why I changed this from a 0 to an i 
                                #First run of the outer loop i = 0 (which is now a row of size 3)
                                #Second run of the outer loop i = 1 (this is still a row of size 2)
        if twodlist[i][j] == 2:
            twodlist[0].append(100)
        print(twodlist[i][j])
        j = j + 1 # OR j +=1 


#twodlist[0] has length 2 initially so range(twodlist[0]) =  [0,1]
#Exit condition for our while is j = len(2dlist[0]) acceptable numbers [0,1]

""" 
One last thing we need to see done before we go on a break 
"""

board = [
    [1,2,3,4], #Row 0
    [5,6,7,8], #Row 1
    [9,10,11,12], #Row 2
    [13,14,15,16] #Row 3
            ]

print(board)
for row in board:
    for number in row:
        print(number, end = " ")
    print()

board = [
    [".",".","."],
    [".",".","."],
    [".",".","."],
]

for row in board:
    print("|",end = "")
    for number in row:
        print(number, end = "|")
    print()

""" 
Now I get to something that looks suspiciously like a tic-tac-toe board.

When we come back: The example I'm going to do is checking for a winner on a tic-tac-toe board

10:20 
"""


""" 

"""