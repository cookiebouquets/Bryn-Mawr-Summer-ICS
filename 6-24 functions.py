"""
The last topic in terms of the python unit is functions. Functions have a lot of nuance to them and they're kind of annoying to deal
with at first. 

What functions allow us to do is create reusable pieces of code so we don't have to keep rewriting things over and over again. They
allow us to create subroutines in our program that are named so we can call the function name and have that subroutine run. 

f(x) = x + 5 <= Takes in a value x and adds 5 to it 
    input = x
    output = x + 5

functions in programming work exactly the same way
print(x)
    input = x (as a string)
    output = printing x to the terminal 

append(x)
    input = x
    output = adding x to our list

int(x)
    input = x
    output = x as a integer 

^These are examples of built in functions in python so whenever you download python you get these by default. Python functions live
in something the namespace 

namespace = all of the reserved words in python + all of the names of function python 

"""
#print(dir()) <= this is how you access the namespace 

""" 
That was a tangent on how functions are stored in python. How do we do something actually useful now? I want to make my own functions.

def <name of your function>(<OPTIONAL: inputs>): <= Function header
    <code block corresponding to your function>  <= Function body 


"""
def hello():
    print("Hello world")

""" 
Now I want to use my hello() function. How do we do this? this works exactly how every function works in python
""" 
hello()
"""
What happens if I don't have the parentheses? 
"""
print(hello)
""" 
It gives us the name of the function at some memory address (not pleasant!) So make sure you have your parentheses whenever you call
a function
"""
print(hello()) #An extra print outside of the function itself will give you weird behavior

""" 
JUST use hello()

Let's say I wanted to introduce some sort of input into our function
"""
def hello(name): 
    print(f"Hello, {name}")

""" 
our inputs BEFORE a program is ran are called parameters. Parameters DON'T need to have a value beforehand. Think of these as x in f(x)

x is a placeholder until we give x some value

f(x) = x + 5
f(5) = 5 + 5

hello(name) = print(hello, name)
hello("John") print(hello, john)
"""
hello("Tim Cheese")
hello("John Pork")
""" 
At runtime the inputs are then called arguments

compare and contrast for hello(name)

parameter = name
arguments = Tim Cheese, John Pork, or any string

f(x) = x + 5
parameter = x
argument = 5,10, or any number
"""
def mean(nums):
    average = 0
    for num in nums:
        average += num
    average = average/len(nums)
    print(average)

numbers = [1,2,3,4,5]
mean(numbers)
numbers2 = [1,8,25,65,100,250]
mean(numbers2)

"""
I've done something here that is bad. Think back to when we first started this class. You need to save your result into a variable 

I just tried to print average later on instead of calling mean() and I got an error. When a function is called, python suspends control
of the program and passes control into the function. When the function is done running, control is passed back to python.

    -python is completely blind to what happened inside the function. This is because of something called scope. 
    -Scope = context for a specific program 
    
    global scope = the entire program
    local scope = the scope inside of an indented code block (for loops, functions)
    for-each loop, we made copies of our variables inside of a list and those copies get destroyed after the for-loop ends. 
    inside of a function, after a function ends, all of the variables we created inside the scope of our function also get destroyed

How do we save objects from the a local-scope of a function? How do we save the result of something in a function? 

return <= you've heard me use this word before. Particularly when I said "input() specifically returns a string"
"keys() returns a list of your keys"

return <optional: data> =
    1) ends the function and gives control back to python.
    2) flags <data> as something to be saved into a variable 
"""

def mean(nums):
    average = 0
    for num in nums:
        average += num
    average = average/len(nums)
    return average
          #3.0


print("With Return")
numbers = [1,2,3,4,5]
avg = mean(numbers)
print(avg)
numbers2 = [1,8,25,65,100,250]
avg2 = mean(numbers2)
print(avg2)


"""
All the stuff that happens in python is unknown to mean

(python) "Alright mean() it's your turn" (numbers) 
 |                                           |
 V                                           V
(mean) "Im going to compute my average" (average)

What mean did to compute the average is unknown to python 

10:30 
"""

def example(num):
    if num % 5 == 0:
        print("Hello! 5")
        return
    
    if num % 3 == 0:
        print("Hello! 3")
        return
    else:
        print("No thanks!")
        return
    
example(5)
example(6)
example(7)
example(15)

""" 
When I say return ends control of a function. It REALLY ends control of the function.

When you declare a parameter inside your function header. They become REQUIRED. 
"""