"""
So it seems like you guys lucked out! I didn't post the homework that was due for today. Instead, we're
going to cover looping statements today, and end with a lab. 



Last time we covered

conditional statements: Things like boolean statements that evaluate to true or false, we used 
if-elif-else for this, and it allows us to run blocks of code that only happen if the conditional statement
evaluated to true

string functions: How to manipulate strings where most importantly we covered lower(), strip() and to concatenate
strings with the use of + 

Lists: Ordered lists of variables, mixed data types, how to add with append(), how to remove with remove() and pop()
also how to join two lists together with extend() 
also how to access things with <name of list>[<index>]
"""

"""
today we're covering looping statements. Which is how we're going to be able to repeat code blocks until some exit
condition is satisfied

There are three kinds of looping statements

while(): <= this is the most natural one to use 
for-i loops: <= allows us to pull out a list of numbers we want to manipulate
for-each loops: <= specific to lists or other objects with indices

we'll cover while loops first

while(<conditional>):
    <Everything you want repeated has to be tabbed over
"""

x = 0
while x < 5:
    print(x)
    x = x+ 1

"""
You'll see in this example, our while loop ran infinitely. Clearly this is a problem because we want the program to 
end at some point or else we'll an error called "Stack Overflow" 

We always need an exit condition for a while loop. 

Exit condition: A piece of code that allows the conditional in our while loop to evaluate to false. 

In our example, our exit condition that needs to satisfied is x >= 5. What's the easiest way to do this? 
Just setting x to 5 only allowed our code to run once which isnt repeating anything. So instead, let's just
add 1 to x each time we execute the body of the while loop

We replaced x = 5 with x = x + 1 which allowed us to repeat our code 5 times. 

Requirements:
    1) while <conditional>: 
    2) a code block underneath that's tabbed over (this is called the body)
    3) Some exit condition that breaks the conditional.
"""

x = 1
while x <= 100:
    if x % 3 == 0:
        print(f"{x} is divisible by 3")
    x = x + 1

""" 
In my opinion the appeal to this is pretty obvious. There is only so much math you can do in your mind, and looping
statements allow us to automate math at superhuman levels. With looping statements, repeating code can be done 
at such extreme levels that they'd be better than any human at the same task.

While loops also allow us to naturally create a repeating menu structure in our program. 
"""
"""
cash = 0
bank = 100

check = True
while check == True:
    print("Welcome to the bank")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. quit")
    print(f"your balance: {cash}")
    print(f"bank's balance: {bank}")
    option = input("Select your option from the list above: ").strip().lower()
    if option == "withdraw":
        bank = bank - 10
        cash = cash + 10
    elif option == "deposit":
        bank = bank + 10
        cash = cash - 10
    elif option == "quit":
        check = False
    else: 
        print("invalid option")

        """
"""
This example is an example of the most common way to repeat a program after we finish one execution


1) print a menu that asks for these 6 options
    1) addition
    2) subtraction
    3) multiplication
    4) divison
    5) modular division
    6) quit
2) a variable called option that tkes in keyboard input
3) if-elif-else that corresponds to the 6 options above
4) You need to introduce a while-loop that runs the program over and over until quit is selected
    a) you need a variable called check = True
    b) when option == "quit"
        a) check = False

"""

"""
Now we're going to cover for-each loops. 

The context is we're given a list and we want to loop over the list. "iterating over". What this does is 
it'll repeat a codeblock over and over again for each element of a list

"""
nums = [10,20,30,40,50]
for x in nums:
    print(x)

""" 
The syntax is

for <name of dummy variable> in <name of list>:
    <code block to be repeated>

What for-each loops do is introduce a dummy variable. What the dummy variable is assigned to is elements of the list

On the first run:
    x = 10 (because 10 is at index 0)
    print(x)

on the second run:
    x = 20 (because 20 is at index 1)
    print(x)

    .
    .
    .

"""

fruits = ["oranges","apples","mangoes","cherries","grapes"]
for fruit in fruits:
    if fruit == "cherries" or fruit == "grapes":
        print(f"{fruit} is a small fruit")
    elif fruit == "apples" or fruit == "oranges" or fruit == "mangoes":
        print(f"{fruit} is a large fruit")

""" 
For loops allow us to manipulate lists "element-wise" (which really means manipulating one object at a time)

"""
nums = [23,13,45,40,87,35,63,22,9,1,50,27,95,100,21,28,38,80,29,53,16,32,60,65,79,8,66,7,70,4,99,78,88,10,46,25,47,93,83,36,56,91,97,96,2,57,26,54,55,98,51,37,17,49,69,72,59,64,77,94,24,82,30,31,39,43,76,92,52,74,11,84,58,67,34,12,41,68,81,85,19,20,44,18,15,14,61,42,3,86,48,75,6,62,89,73,90,71,5,33]
total = 0
for num in nums:
    total = total + num 
print(f"sum of nums is {total}")
"""
We know the average to be the sum of all of the numbers/amount of individual numbers 

len(nums)
"""
amt = len(nums)
avg = total/amt
print(f"The average of the numbers is {avg}")

"""
for-i loops pull out individual indices from our list. The first thing that needs to be introduced is the range function

range(<integer>) = creates a list of numbers from 0 to <integer>-1

Lists are indexed from 0 to len(list)-1

range(len(list)) will give us all of the numbers from 0 to len(list) -1 <= all of the possible indices of our list
"""
nums = list(range(100))
print(nums)
nums = list(range(5))
print(nums)
"""
The "range object" from when we just ran nums = range() is what we actually need for our for loop. 
"""

mylist = [5,7,1,3,6,8,2,10]
nums = list(range(len(mylist)))
print(nums)

total = 0 
for i in range(len(mylist)):
    total = total + mylist[i]

print(total)

total = 0
for num in mylist:
    total = total + num
print(total)

"""
How is this more useful/a for-each loop? 

Let's say I'm creating a program that adds 2 to all our numbers in our list

first with a for-each and second with a for-i
"""
mylist = [1,2,3,4]
for num in mylist:
    num = num + 2

print(mylist)
"""
What the heck? I still got my original list back. That's not the behavior we wanted, so what happened?

For-each loops create COPIES of our object in our list. In a for each loop

num =/= mylist[i]

In our example, we weren't adding two to each number of our list, what we were doing is adding 2 to a COPY of each number
in our list.

In order to fix this, we should use for-i loops because they access the list directly. 
"""

mylist = [1,2,3,4]
for i in range(len(mylist)):
    #Remeber that i is set to a value between 0-3
    mylist[i] = mylist[i] + 2

print(mylist)

"""
Instead of creating copies with a for-each loop, we created a new variable i that gets assigned to the values
0,1,2,...,len(list)-1 

which allowed us to manually access the list using mylist[i] which modifies the list instead of the copies. 

range(number) = [0,...,number-1]

mylist = [1,2,3,4]
          0,1,2,3
range(len(mylist)) = [0,1,2,3]

for num in mylist <= creates copies of element in our list

for i in range(len(mylist)) <= creating copies of [0,1,2,3]
"""

"""
Concurrent Lists

What commonly happens in programs is you will have two lists that are related contextually but they're separate variables

1) List of Fruits
2) The quantity of your fruits

1) List of fruits
2) the prices of each fruit

1) a list of account names
2) the balances of each account

How do we tie these two lists together if they're separate variables. 
"""

fruits = ["orange","mango","grapes"]
prices = [1.25,1.50,2.25]

""" 
How are these two lists exactly related? 

1) Lists have three things attached to them
    1) the name of list 
    2) The actual objects in the list
    3) The indices of each object in the list


We can match the objects of each list based on their index. For example:

1) Oranges have the price 1.25 <=> fruits[0] and prices[0]

I want to write storefront program that just prints all of the fruits and their prices. 

Which kind of for-loop is useful here? HINT: there's two lists so one of the kinds might not work

for-i loop: We know the two lists are related based on the indices of each object. So that means we should be 
iterating over our indices rather than individual objects because there's no way we can really fit two for-each loops
in a way that makes sense

"""
print("welcome to our store")
for i in range(len(fruits)):
    print(f"Fruit name: {fruits[i]}")
    print(f"Fruit Price: {prices[i]}")

"""
Strings are really just lists of individual characters.

We can do for-loops over strings and look at individual characters
"""

code = "aabbbabbabababbabbabbababababbabbabbabbaabbaaababaababaaabaaababababababaaaabab"
total_a = 0
total_b = 0

"""
How many individual a's and b's are in this code? 

In computer science, the common way to denote single characters in a string: char 

In other programming languages, char is its own data type, but in python, chars are just one character strings
"""

for char in code:
    if char == "a":
        total_a = total_a +1 #this
    elif char == "b":
        total_b += 1 #This a shortcut

print(f"Total a's: {total_a}, total b's: {total_b}")

"""
I can create new strings by concatenation using +. 
"""

str1 = "hello"
str2 ="world"
print(str1 + str2)

"""
Addition of strings is not commutatitve
"""
print(str2 + str1)

strcopy = ""
for char in str1:
    strcopy = strcopy + char
    print(strcopy)


"""
Our lab is to check whether or not a word being inputted is a palindrome. 

A palindrome is a word that's spelled the same way backwards

noon is a palindrome
racecar is a palindrome
Extra Credit: taco cat is a palindrome 

moon is not a palindrome
computer science is not a palindrome 

Using for-each loops, check to see if a word the USER types in is a palindrome


"""
#word = input()
#copy_backwards = ""
#for loop here

#if word == copy: 
    #print(f"{word} is a palindrome")


str = ""
sentence = "This is a sentence".split()
newstr = "".join(sentence)
print(newstr)


word = "taco cat".split()
word = "".join(word)
print(word)


"""
last class i said .join() is useless. How it's actually useful is specifically this case. 

.split() = takes in a string and creates a list of strings where each element is split at the whitespace

sub.join(<str>) = takes in a list and creates a new string where each element of the list is joined together by the string 
in the subject


str = this is a sentence 

this sub is sub a sub sentence

" " 
this is a sentence
#
this#is#a#sentence
""
thisisasentence
"""
