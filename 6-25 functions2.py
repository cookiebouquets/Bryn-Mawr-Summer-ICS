"""
Today we're going to cover more important details about functions and then implement an example final project 

So last time
    - Dictionaries: which I showed to be a sort of enhanced list, with key-value pairs rather than elements that are accessed
    with a index. Keys could only be immutable objects, so things like strings, numbers, etc and values could be anythign
    - Functions: Reusable segments of code that have a name
        - return statement 
        - global vs local scope

    - Difference between pass by value vs pass by reference <= the last thing we cover in the python unit 
    
    - Thursday is just working on our individual final projects during class time and if we have any question's I'll be here.
    Due Friday 11:59 PM

    Connect 4
        - Checking for winners in connect 4 is the pretty much the same as checking for winners in tictactoe but the board
        is bigger than 4x4. So in tictactoe we could just check the entire for a winner. So you need to do for-loops over the entire
        board to check for a winner (this comes with some tricky parts when you're accessing parts of a 2D list)

        X00XXX X <= index out of bounds errors
        0X0000
        00X000
        000X00 
             ^= index out of bounds errors 

        You can only fall off 3 places on connect4, the very bottom, the very far right, and then bottom-right corner 

        - Gravity for pieces: The easiest way to do this is with a while loop that checks what the current slot is 

        000000
        000000
        000000
        000000

        Checking for the first occurence of not a placeholder OR you the bottom of the board 


    Friday: Number systems
        - Base 10, you have a ones place that ranges from 0-9 
            - Binary, Base 2
            - Hexadecimal, Base 16
            - How to convert between Base 10 to Binary, Binary to Hex, Base 10 to Hex, etc. 
            - Discussion on where these show up
        - less on the programming side and more on math 

    Mon-Thurs: Arduino
        - Arduino is programmed in C, for the sake of the class, we don't have to use really complicated C. 
        - Hardware Programming (Making LEDs turn on and off, passing power into a servo motor, messing with sensors)

"""

"""
Pass by value vs pass by reference:

"I'm passing something into a function"  <= my function has a parameter and I pass in the argument as the parameter 
"""

def example(num):
    print(num + 1)

example(5) #<= Passing in the number 5

""" 
Weird things happen when we pass certain kinds of data into a function

"""

def example2(num):
    num = num + 10
    return num

number = 15
print(number)
number = example2(number)
print(number)

""" 
Something weird happened here:
    - I created a variable called number
    - I passed in number as the argument of our function example 2
        - example2 takes our number and adds to 10
    - We expect 25 to be printed after example2(number)
    - We got 15 as our print

This is weird, why did this happen?

When python communicates with example2, all that gets communicated is the value of number and not the variable number 

value of number vs the reference of number. example2 doesn't know the reference of number so it can't update the variable number 

everything that exists inside a function only exists within that function and nothing outside of the function exists within the function
as well (global vs local scope)
"""

def example3(mylist):
    mylist.append("Hello from example3")

strings = ["Hello","World"]
print(strings)
example3(strings)
print(strings)

"""
Something weird has happened here: in our previous example where we added 10 to number, number didn't get updated. However, 
when we passed in a list and updated the list, it did get updated even though mylist =!= strings IN NAME ONLY

when we pass in a list (or any mutable object), then we're passing in the reference of the list itself (so both python and example3
know the address of our list).

Things get passed in as value (immutable):
    - Integers
    - Floating point numbers
    - Booleans (true or false)

Things get passed as its reference (mutable):
    - Lists
    - Dictionaries 
"""