""" 
Notes for Homework PSET 1
"""
#num1 = 75
#num2 = 60
#print(num1 // num2)

# num3 = int(in())  <-- this wont work
# num3 = int(input()) <-- this will work 

""" 
In yesterday's class I introduced you to a lot of basic python syntax 

-how to print() to terminal
-Variables, specifically integers and strings
-How to manipulate integers
-how to accept keyboard input via the input()
-Typecasting our data coming in from input()

Today we're going to expand on this topic and work with the other primitive data type (Booleans) 

Booleans are statements that can be evaluated to True or False
Booleans are just True or False
"""

var1 = True #In python, True has to have a capital T and False has to have a capital F

""" 
Booleans allow us to branch out our program into different paths. Booleans also come with something called

if-else logic, which allows us to branch our program into different paths. 
"""

if var1 == True:
    print("Hello Class")


"""
Variable assignments are specifically ONE equals sign, and checking for equality is TWO equals signs. 

Anytime you have a colon in python, you need to indent the lines below. Just by checking our logic, we should expect 

"hello class" to print because on line 26, we set var1 = true and true == true, which is clearly true. The next thing you need to be 
careful of, is if you want to exit the code block, you need unindent your code. 

Basic syntax:

if <conditional statement>:
    <code below has to be indented>
"""

var2 = False
if var2 == True:
    print("Hello 2")
print("hello 3")

""" 
Just checking whether a variable is equal to true or false is not exactly the most useful. if-statements are capable of checking
any conditional statement 
"""
var3 = 5
if var3 >= 4:
    print("hello 4")
print("hello 5")

""" 
for numerical conditionals, we can use >, <, >=, <=, ==.

We can also do arithmetic in the conditional statement before evaluating to True or False. 

I want to check if a number that's taken in via input is even or odd. 

num % 2 == 0 <= the number is even
num % 2 == 1 <= the number is odd 

num = int(input("Enter your number: "))
if num % 2 == 1:
    print(f"{num} is an odd number")
else:
    print(f"{num} is an even number")

    

What if our number is even and we wanted to print it?  So just having the print statement be outside of the if-statement doesn't exactly
capture behavior we want. 

Having two if statements does what we want it to do, but in some cases, having two if-statements can lead to unexpected behavior 
^ have to revisit this later, but we'll still introduce the else keyword.

Rather than having two if-statements, what we can do is introduce else: instead. 

What else: does, is if the if-statement fails to evaluate to true, all other cases will filter into the else. There's one last keyword
that is important here: elif. 

elif basically takes an else and if statement and combines them together into one word. In other programming languages, you're gonna 
have to write else if as both keywords, but python has shortcut that lets you perform elif in one keyword. 
"""

"""
print("checking if a number is divisible by 5 or 2")
num = int(input("Enter your number: "))
if num % 5 == 0:
    print(f"{num} is divisible by 5")

if num % 2 == 0:
    print(f"{num} is divisible by 2")
else:
    print(f"{num} is not divisible by 5 or 2")

num = int(input("Enter your number: "))
if num % 5 == 0:
    print(f"{num} is divisible by 5")
elif num % 2 == 0:
    print(f"{num} is divisible by 2")
else:
    print(f"{num} is not divisible by 5 or 2")
"""

""" 
as soon as a statement gets evaluated to true in a if-elif sequence, everything afterwards gets ignored. This example is why 
you need to be careful in whether or not you are going to use two if-statements or if-elif. 

if's and elif's can be useful for creating a menu structure for our program. I'm going to write a program that has different outputs
depending on the input. 

print("Welcome to our baltimore sports program")
print("1. Football")
print("2. Baseball")
option = input("Enter the sport you would like the know the Baltimore Team for: ")
if option == "football":
    print("Baltimore Ravens")
elif option == "baseball":
    print("Baltimore Orioles")
else:
    print("no valid option for that sport")


One thing you need to be careful of is that string matching is exact. In our example, we were checking specifically for 
lowercase football and lowercase baseball. There's a way we can work around this, but it'll be in probably an hour when I go over
string functions. 

We're going to revisit the calculator program. Originally we just did all 5 operations in a straight line, all of them evaluated. 
That's not actually how using a calculator works: we want the user to be able to choose which operation they are allowed to use.

What we're going to do is modify our calculator program AGAIN, but we're going to introduce a menu structure by using if-else logic.

1. Go back to your calculator program (make a new file)
2. make a menu with print statements 
    welcome to our calculator:
    1. Addition
    2. Subtraction
    3. Multiplcation
    4. Division
    5. Modular division
3. Create a variable called option that takes in keyboard input for those 5 options
4. use if-elif-else for each of those operations. 

If i type in addition, i should get the addition logic to run 
"""

"""
print("welcome to our calculator:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplcation")
print("4. division")
print("5. modular division")
option = input("Enter the operation you would like to do: ")
if option == "addition":
    num1 = int(input("enter num 1"))
    num2 = int(input("enter num 2"))
    sum = num1 + num2
    print(f"the sum of {num1} and {num2} is {sum}")
elif option == "subtraction":
    #pass means you should fill this in with the correct logic
    print()
elif option == "multiplication":
    print()
"""


"""
You should write your code and test it in full functional chunks
"""


""" 
The next thing we're going to cover today are Strings.

In programming, you can do more stuff with strings than just print them. We are pretty familiar with printing them and taking them
in as an input via the input() function. They're a little bit more nuanced than we think they are.

For example: for our menu structures in our programs, 

if option == "some string":

for this if statement to evaluate to true, we saw that it has to specifically be "some string" and not "Some string" or "some String"
or even " some string" or "some string "

matching with strings has to be exact in a painfully pedantic way. This is because strings are actually lists (which i'll show at 
the end of class today).

so strings have a few functions that are associated with them. The most relevant one right now is .lower() '

.lower() = makes a string entirely lowercase 
"""

text = "HELLO WORLD"
print(text)
text = text.lower()
print(text)

""" 
You might notice something strange. How come in line 210, I had to assign text back into itself? That's because text.lower() doesn't
actually modify the original string, it actually creates a new string that you have to assign to a variable. 

lower() does NOT edit, all it does is create a copy of your lowercase string. 

There are still some cases where it kinda doesn't really matter and thats in checking booleans. 
"""
print("test menu")
print("1. hello")
print("2. world")
option = input("Enter your option: ").lower().strip()
if option == "hello":
    print("hello")
elif option == "world":
    print("world") 


"""
lower() makes the ENTIRE string lowercase.

Similarly, there's a function that makes a string entirely uppercase. 

upper() makes a string entirely uppercase

Note on syntax: <name of string>.<function>() 
                    subject       verb   (<object>)

text = "hello world"
print(text)
text = text.upper()
print(text)


upper() is not really as useful even though its functionally the same thing as lower() because in our minds, lowercase letters are 
significantly more common. 

Like i said before, string matching is exact "hello" is not the same thing as "hello " or " hello". We can account for user error
in a menu by using this next function.

strip() = removes all whitespace as the beginning and end of our strings. 
"""

text = "           hello"
#print(text)
#text = text.strip()
#print(text)

"""
from our option menu from before, we had issues with " addition" or "addition ". We can call .strip() on our option variable and 
remove all extra whitespace if there is any

.lower() and .strip() are 

whenever you want to use a function, we say we're calling a function. Whenever you call a function () MUST be at the end of the 
function name
"""
print("hello".upper())

""" 
all of our functions are saved in what's called the namespace of a program. the namespace is basically all of our keywords and functions
and they're stored in our computer's memory (RAM) The bottom line is make you have your parentheses 

if we strings and we wanted to put them together as one string, we can accomplish this in two ways:

1) string1 + string2 = string1string2
2) .join() = it will join two strings together 
"""

str1 = "hello"
#       012
str2 = "world"
print(str1 + str2)

""" 
String addition is not commutative 

str1 + str2 =/= str2 + str1 <== this fact is highly important 
"""
print(str2 + str1)

""" 
.join() is a function that you call from a string and requires an object inside the parentheses

str.join(some other string) <== creates a new string where each letter from the "some other string" gets separated by "str"
"""
newstr = str1.join(str2)
print(newstr)
"""
say i wanted to print out "w o r l d"
"""
newstr = " ".join(str2)
print(newstr)

""" 
find() = finds the first occurence of a substring and returns the position where it's found
"""

index = str1.find("l")
print(index)

""" 
Why did str1.find("l") return 2? Lists in computer science don't start from 1, they actually start from 0. This is useful when you're 
scanning a text that's thousands of characters long and you need to find the occurence of a substring in there. 

strip() 
lower() 
upper() 
find() 
join() is a weird one that might show up in later classes 
"""

""" 
We want to modify our calculator program one last time in this scenario: call .strip() and .lower() on your input so you can account
for user typos. 

10:15
"""