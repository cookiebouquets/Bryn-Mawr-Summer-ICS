"""
Last time:

    - Nested For loops
    - 2D lists

Today:

    - Dictionaries: These are slightly enchanced versions of lists
    - Custom Functions: There's a lot of nuance that comes with this 
    - After custom functions we'll circle back to tic tac toe and finish that
    - end of class: If there are any questions wrt PSET 2 or what to do for the final project then we can cover that at the end

"""

"""
Dictionaries (in other programming languages and usually on the internet, they're called hash tables) are also a way to store
multiple pieces of data inside one named variable.

The only thing we have so far to do this are lists. A thought exercise that motivates the use of dictionaries is if we had our olive garden
example but instead of the second list being sides, we had a second list that corresponded to the prices of all of the entrees
"""

entrees = ["Steak","Pasta","Grilled Shrimp"]
prices = [25,18,19]
         #0,1,2
""" 
At the end of class last friday we correctly observed that entrees and prices are related through the indices of their objects 

"""

"""
for item in entrees:
    for price in prices:
        print(f"Entree: {item} Price: {price}") 

        
"""
print("-----")
    
for i in range(len(entrees)):
    print(f"Entree: {entrees[i]} Price: {prices[i]}")

""" 
We're familiar with this example but it's a little unsatisfying I feel because we're really leveraging the fact that entrees
and prices share indices. That's not a concrete relationship between the two lists 

We're sort of enforcing this relationship between entrees and prices implicitly which might get confusing with a program that's
more complex

Dictionaries get around this "Two lists running parallel" weirdness by introducing something called Key:Value pairs 

Dictionaries are lists where each value no longer has an index but instead has a "key"
"""
entrees = {"Steak":25,"Pasta":18,"Grilled Shrimp":19}
          #<Key>:<Value>

""" 
Now each entree is related to its price inside one data structure rather than having two data structures running in parallel

"""
print("---")
print(entrees)

"""
We need to cover the same basic stuff:

    1) How do we pull out individual items from a dictionary?
    2) How do we add items to a dictionary
    3) How do we remove items from a dictionary? 
    4) How do we iterate over a dictionary? (How does a for-loop work over a dictionary?)

1) We can use the square bracket operator but instead of an index, we type in the key. In our example, "Steak" is a key and 25 is a 
value
"""
print(entrees["Steak"])
""" 
How do we get the keys out of the dictionary? You should know what the keys are beforehand so you can just print out the string by itself
with no relation to the dictionary

If somehow you don't know the keys: You can use the .keys() function

dict.keys() <= Returns a list of all of the keys in our dictionary 

We know the keys to be "Steak","Pasta","Grilled Shrimp"

If i call entrees.keys() <= ["Steak","Pasta","Grilled Shrimp"]
"""
print("Steak")
keys = list(entrees.keys())
print(keys)
print("---")
""" 
2) How do we add items into our dictionary? This is a little more nuanced than you expect it to be.

In a list we just did <nameoflist>.append(item) <= doesn't exist for a dictionary. We have to use the square bracket operator again
to add to our dictionary

General syntax:

dict[<new key>] = <new value> <= Basically the same thing as a variable assignment 

dictionaries are unordered. The information on your computer is not stored sequentially so there's 
    1) No point to storing things in a specific order because keys have no implicit order to them
    2) Your key:value pairs aren't stored sequentially on your computer's memory as opposed to a list 

"""
entrees["Lobster"] = 60
#This will create a new key:value pair where the key is "lobster" and the value is 60
print(entrees["Lobster"]) #Will print out 60
print(entrees)
"""
There is some nuance to what kind of keys are possible.

Two kinds of ways data can be manipulated

    1) Mutable: objects that can be modified without having to do a variable reassignment 
            a) Lists are mutable (we could do .append(), .remove(), etc. without having to use a variable assignment operator)
            b) dictionaries themselves are mutable (we could add to dictionaries)
    
    2) immutable: objects that can't be modified without having to do a variable reassignment 
        a) numbers: integers, floats, etc. 
            total = 0
            total +=1 
            total = total + 1   
        b) Strings
            Even though it had built in functions that modified the string, we had to re-save it back into itself using a variable
            assignemnt 

            
Most of the edge cases I've mentioned so far come down to the fact that some pieces of information are mutable and some pieces 
are immutable. This concept is probably one of the most important things in computer science (the theoretical discipline) and 
you'll probably see it again if you go on to take AP CS A

The things that can be keys are immutable objects

Keys can be numbers or strings <= For the sake of the class this is what's important to know 
"""

mydict = {1:15,"Hello":"World",2.5:10, 3:"Olive Garden"}
print(mydict)
""" 
Dictionaries are unordered for the reason that numbers can also be keys. 

mydict2 = {[1,2,3,4]:"Hello World"}
print(mydict2)

unhashable effectively means mutable. So the reason why keys have to be immutable is because a dictionary is effectively like a 
phone book. 

How a dictionary works is it'll look inside the phone book and search for the address of the key -> value. If your object was mutable
then your phonebook will no longer be accurate because when you change something about a mutable object, then the address of the object
will change and your phonebook won't point to the correct place in memory. 
"""

""" 
What can be values? Pretty much anything. Numbers, Boolean Vaues, lists, other dictionaries, etc. 
"""
print("----")
mylist = [1,2,3,4]
         #0,1,2,3
mydict2 = {}
mydict2["List"] = mylist
print(mydict2)


""" 
This bizarre. How do we pull out objects from our list inside of our dictionary? What we can do is use two square brackets. 
"""
print(mydict2["List"][1])

"""
That works maybe not exactly how we expected it to but definitely in a way that's related to something we've seen before?

"""
student = {"Name":"John Smith","Grade Level":9,"Email":"SmithJ@BrynMawrSchool.org"}
grades = {"English":65,"Math": 100,"Social Studies":85,"Biology": 70}
student["Grades"] = grades

""" 
I want to know what his English Grade is. How do we print out his english grade
"""
print(student["Grades"]["English"])
""" 
We can pull out values from nested dictionaries the same way that 2D Lists work
"""
mydict3 = {"Hello":"World"}
mydict4 = {"Mylist":[1,2,3,4]}
mydict3["subdict"]= mydict4
""" 
Drawing a diagram of what's hape
mydict3 {"Hello": World}
        {"subdict":mydict4} -> mydict4 {mylist:[1,2,3,4]}
                                               #0,1,2,3
print the number 2. How do we print the number 2? 
"""
print(mydict3["subdict"]["Mylist"][1]) #Fun thought exercise in how to pull out a number from a nested dictionary inside a nested list
"""
Let's say lobster is no longer on the menu
"""
print("---")
print(entrees)
""" 
I can remove something from a dictionary using .pop()

we've seen .pop() <= list.pop(<index>) 

dictionary.pop(<Key>)
"""
entrees.pop("Lobster")
print(entrees)
"""
How come there is no .remove() for dictionaries? 

For a list .remove(<value>) takes in a value

Values are not unique in a dictionary, the keys are unique
"""
entrees["Ribs"] = 18
print(entrees)
"""
Ribs and pasta both point to the value 18, so .remove(18) wouldn't make sense here because two keys point to the same value 
and python wouldn't know which one to get rid of 

9:20
"""

"""
The last useful thing about dictionaries are for-loops over them.

for-each loops and for-i loops: for dictionaries just pretend for-i loops don't exist at all because for-i imply some sort of order
but dictionaries are inherently unordered. The only thing we can do are for-each loops

"""
print("----")
for item in entrees:
    print(item)

"""
For each loops pull out specifically keys. I said something along the lines of "for-each loops make copies of objects and you can't
directly modify lists as a result a for-each loop" 

^ does not actually apply to dictionaries. Logically that makes sense because for-each loops pull keys out of dictionaries and the thing
we might want to change are the values. We can use a square bracket operator to access the values (which we can then change)
"""

for item in entrees: #< THIS WON'T MAKE COPIES SO WE CAN MODIFY THE DICTIONARY WITH TIS
    print(entrees[item])

"""
In order to access values in our dictionary we need to use a square bracket operator still even inside for-each loops. If we're married
to the fact we want copies of the values 

dictionary.keys() that makes copies of all of the keys. 
dictionary.values() that makes copies of all of the values. <= in my mind this is not super useful 
"""
print("Using values()")
for item in entrees.values(): #<THIS WILL MAKE COPIES SO WE CAN'T MODIFY THE DICTIONARY WITH THIS
    print(item)

print("Raising prices")
for item in entrees:
    entrees[item] += 5 #Adds 5 to all of the values of our dictionary

print(entrees)