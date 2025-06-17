""" 
What is really computer science and why do we care at all about it. 

Computer Science = The automation of tasks that we can perform algorithmically. 

The main thing that separates a computer scientist from a regular person is not the ability to code
but moreso the ability to think algorithmically. 

Thinking Algorithmically = Breaking down a process into actionable steps. 

The goal at the end of this class is not necessarily be able to write fantastic python code
or make great arduino projects, but really be able to think about our problems in terms of steps
and algorithms. 

Even if we're not interested in STEM or computer science, being able to code or think like a computer
scientist is important because it shows up in a lot of different occupations. 
"""

""" 
In this class, we're going to learn how to write code in python. Python is probably the most 
popular computer programming language right now. 

Why python is popular:

1) It's pretty easy to pick up
2) It's adaptable to a lot of tasks

Python is used in machine learning, AI, Statistics, basic scripting, and a lot of different business
functions 

About Python:

Python is called an interpreted language.

There are two different kinds of programming languages: Interpreted or Compiled

Interpreted Languages = Convert Python Code into machine code line by line while running 
Compiled Languages = Covnert Code into machine code all at once before running

Examples of compiled languages = C, C++
Examples of interpreted Languages = Python, Javascript, C#

When we write programs, we are basically writing english that gets converted into something called machine code. 
What machine code is: Binary Numbers that corresponds to actions that we can perform that manipulate the memory on our 
computer.

The first thing we're going to work on is variables and datatypes.
"""
#print("hello World")

"""
The only thing we've done so far is printing hello world. That is like not useful at all on it's own. 

What we really want to be able to do is manipulate things like numbers, text, lists of numbers, true/false, etc. 

These things are called data types. More formally, we say

numbers are really integers (whole numbers including negative numbers) /floating point numbers (decmial numbers)
text are really called strings (strings of individual characters)
true/false values are really called boolean values (evaluating statements to true or false)

integers = whole numbers including negatives
strings = text

"""
print(5 + 10)

""" 
Common pitfalls for this not working: if you put quotation marks, then print() will interpret "5 + 10" as a string, and 
just print "5 + 10" but not the result 

Strings specifically have to have quotation marks 
"""

print("This is a string")
print(5 * 10)
print(10/ 5)

"""
We can print basically anything we want. But this also, is still not exactly the most useful thing. 

Printing to the terminal =/= Saving the result of the math to be reused. We need to find a way to save these results
so we can reuse them or reference again later on. 

The way we do that is by using things called variables.

Variables are named places in memory (RAM) that store data. Variables contain two pieces of information with them:
1) The data itself
2) The data type

Knowing the data type is important because when we were printing something, there was a functional difference between
5 + 10 and "5 + 10"

"""

number = 10
#<Name of the Variable> = <The value you want to save> 

"""
What number = 10 means, is python will look for a place in memory, give it a name, and save 10 into that name.
Variables are kinda like houses that an address. I want to store 10 in a box that has the address "number" 
"""
print("Printing number:")
print(number)
#print(<variable name>)
"""
What happens if we want to use number elsewhere?  
"""
num2 = 5 
print("Sum of number and num2")
print(number + num2)

"""
Once again, this sum is not useful on its own because we're just printing it. How about we save the result of number
and num2 into a new variable
"""
sum = number + num2
print("sum variable")
print(sum)

""" 
Print() is a function:

<name>(<object>)

We can save more into variables than just numbers. We can save text data (strings) into variables
"""
name = "Jack Basmaci"

""" 
The quotation marks inform python that its looking at a string
"""
print("printing name")
print(name)

""" 
We can save numbers and strings into variables. What happens if we reuse the same variable name? The variable name is
unique, you can't save more than one thing into the same variable name. 

If i wanted to save a new thing into the variable number, I will lose what is currently stored there. 
"""
number = 10
print(number)
number = 25
print(number)

""" 
So let's practice with manipulating integers primarily. What I want you to do:

1) Make a new file, save it as calculator.py
2) make two variables, num1 and num2. Add them together and save the result into a variable called sum. print sum
3) Do the same thing, but with num 3 and 4, but do multiplication instead
4) Same thing, num 5 and 6, but division
5) same thing, num 7 and 8, but subtraction
6) Same thing, num 9 and 10, but perform modular division.

Modular division = Like regular division, but the result is the remainder. 

When performing modular division, we say <num1> mod <num2> 
and what it does saves the remainder after the division. The symbol is percent sign. 
"""
print("modular division")
print(10%2)

num1 = 5
num2 = 10
sum = num1 + num2

"""
Saving into a variable or assigning into a variable 

"Save the result of adding num1 and num2 into sum" or "assigning sum to num1 + num2" 
"""

""" 
Right now, we can make variables, do basic arithmetic, and also print strings. That's great, but we can't interact
with the program in any meaningful way. After we wrote the code, we can't change any of the variables after its ran.
The only we could change variables is if we rewrote the variables before running them. 

We want to be able to have a back and forth interaction with the computer while its running. The first way we can do this
is by using the input() function.

input() is a function that takes in a string as the object which will become the prompt. Then, python will give control
of the program to the user and wait for keyboard input into the terminal, and then assign the result of the input into 
a variable.

print(<object>) prints <object>

input(<object>) prints <object> then waits for keyboard input

what <object> ends up becoming your prompt to the user.
"""
#print("demo'ing input")
#name = input("What is your name? ")
#print(name)

"""
Now that we can take in input and manipulate it, let's try doing some math
"""
print("input and math")
num1 = int(input("type in num 1: "))
#Functions in python evaluate inside first. input() goes first, then int()
num2 = int(input("type in num 2: "))
sum = num1 + num2
print(f"The sum of {num1} and {num2} is {sum}")

"""
What the heck, I typed in 20 and 10, and expected 30 as the sum, but instead, I got 2010. Input() specifically saves
strings.

print(10 + 5) and print("10 + 5")
 15                 10 + 5

 num1 "20" but the data type is a string
 num2 "10"  but the data type is a string

 addition for strings, ends becoming concatenation, which means we add the string to the end of the other. 

 "20" + "10" = "2010" 

 We can fix this very easily with a technique called typecasting. What typecasting does is takes in a datatype and converts
 it into another as long as the data is valid in both data types.

 "20" and 20
 "20" -> 20

 20 -> "20"   

 converting strings into numbers; int()     
"""

"""
Format strings: How do we print a variable in the middle of a string

"The sum of <num1> and <num2> is equal to <sum>". We can use a technique called f strings. What f strings do
is allow us to print a variable inline with other string data. 
"""

"""
Redo the calculator program, but instead of hardcoding the numbers, use input() and f-strings to allow for user input
and better looking text for output 

sum: addition
product: multiplication 
quotient: division
sum: subtraction
remainder: modular division 

That should be it for the rest of class today. I'll post two assignments on canvas, 

1) post the link to your modified calculator program on github
2) The actual homework, which will be some small programs practicing inputs, variables, strings, etc. which will be due
Wednesday at 11:59 PM I'll try to have this posted by 5 pm today. 

"""

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
sum = num1 + num2
print(f"The sum of {num1} and {num2} is {sum}")

name = "Jack Basmaci"
gradelevel = 12
email = "Basmacij@Brynmawrschool.org"
print(f"my name is {name}, my grade level is {gradelevel}, my email is {email}")