""" 
Starting a new file for this next section

So far we've covered if-statements and random functions for strings. The last pivotal data structure we can create (within the scope
of this class) is called a list

If we wanted to aggregate a lot of data in one place in our program, with what we know so far, it'll be kinda clunky and unintuitive

the only way we can do it right now is by making a bunch of variables. We can get around this with a data structure called a list

List = a list an ordered, changeable, set of objects 

basic list syntax is

<name of the list> = [<object1>,<object2>,...,<object n>]
                       index 0,  index 1,      ,index n-1
I alluded to before, lists start from index 0. 

Index = the position of an object within a list.

We use the index to access stuff from our list.
"""

fruits = ["mangoes","bananas","apples","strawberries","grapes"]
          #index 0

""" 
What index is strawberies at? 3. lists starting at index 0 is a huge pitfall for some students, a lot of off by one errors can occur 
here


we can access elements from a list by using the square bracket operator 
"""
print(fruits)
print(fruits[3])

""" 
<name of list>[<index>] <= pulls out object from <name of list> at <index> 

I can also change objects at specific indices 

plural of index is indices 
"""

fruits[3] = "raspberries"
print(fruits[3])
print(fruits)

""" 
What happens if I want to add a fruit? 

<name of list>.append(<object I want to add>) 
"""
fruits.append("strawberries")
print(fruits)

""" 
If we wanted to add strawberries back in at index 3, we use insert() 

<name of list>.insert(<index>,<object>)
"""
fruits.insert(3,"strawberries")
print(fruits)

""" 
Lists can have duplicate objects <= there are other data structures similar to lists that don't allow duplicates.
"""

mylist = [2,3,4,"Jack Basmaci", True]

print(mylist)

""" 
Python lists can have multiple data types at once. HEAVILY EMPHASIZE that this is really weird. Lists typically have one specified data
type. 

My opinions for best practices: Only store one data type in a specific list. 
"""
"""
To remove something we can use .remove() and also .pop()

<nameoflist>.remove(<SPECIFIC object>)
<nameoflist>.pop(<INDEX of the object you want to remove>)
"""
#mylist.remove("Jack Basmaci")
#print(mylist)

"""
Removing something from the middle of the list moves everything after that object over to the left.
"""
#mylist.pop(3)
#now True is at index 3 which gives an error 
#print(mylist)

""" 
Index errors are potentially the number one error that happens for computer scientists 
"""

""" 
There are other ways to access specific elements. Square bracket operator accepts a number for the index, but it also accepts
negative numbers 
"""

print(mylist[-1])
print(mylist[-2])

""" 
Negative numbers allow us to access objects at the end of the list. 

"""
#option = int(input("Which object of your list would you like to access? "))
#print(mylist[option])

"""
Negative numbers allow us to guarantee we get the last object, if we don't know the contents of the list before runtime, we can't
guarantee that knowledge exists.  

- make lists
- add things to them
- remove things
- we can change them via square brackets


"""
mylist2 = [10,15,20,55]
print(mylist2[0] + mylist2[2])

""" 
If the square bracket notation is confusing, you can think of <list>[<index>] as an individual variable name.

"""

mylist3 = mylist + mylist2
#This is the exact syntax as adding strings together 
print(mylist3)

""" 
extend() = adds list2 onto the end of list1 AND SAVES IT BACK INTO LIST1

<name of list>.extend(<name of list2>) will extend <name of list1>
"""
mylist.extend(mylist2)
print(mylist)

""" 
adding lists creates a NEW list, extending one list just makes a bigger list in the name of the original variable

This introduces some trickiness: mylist and mylist3 are identical lists after mylist3 = mylist + mylist2 and mylist.extend(mylist2)

They're actually TWO distinct places in memory. Variables are named places in memory 

mylist3 and mylist are two different places. If I change mylist3, mylist is going to remain unchanged 

"""
mylist.pop(-1)
print(mylist)
print(mylist3)

""" 
Be careful of extending versus adding as adding creates a new variable altogether. Just to make matters more confusing: 


"""
print("confusing example")
num1 = 5
num2 = num1
#Now num2 = 5
num2 = num2 + 5
#Now num2 = 10, because num2 = 5 initially, and 5 + 5 = 10
print(num2)
print(num1)


"""
Copying the value from num1 into num2 and modifying num2 did not change num1. This is not the case for lists 
"""

mylist = [1,2,3]
mylist2 = mylist

""" 
I tried to copy mylist into mylist2 and edit. However, edits to mylist2 also affected mylist1. What's actually happening under the hood
is mylist2 is just a pointer to the address of mylist

mylist 
^
|
mylist2 = mylist

How do I actually make a copy? 

copy()

<name of new list> = <list you want to copy>.copy()
"""
mylist2 = mylist.copy()
mylist2.append(4)
print(mylist)
print(mylist2)

""" 
The exercise that I want you guys to do: 

Calculator with Lists.py

    1. Create a list called nums
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
nums = []
print("menu")
print("menu")
print("menu")
print("menu")
print("menu")
option = input("select your option: ")
if option == "1":
    num1 = int(input("1"))
    num2 = int(input("2 "))
    nums.append(num1)
    nums.append(num2)
    sum = nums[0] + nums[1]
    nums.append(sum)
    print(f"The sum of {nums[0]} and {nums[1]} is {nums[2]}")
elif option == "2":
    num1 = int(input("1"))
    num2 = int(input("2 "))
    nums.append(num1)
    nums.append(num2)
    sum = nums[0] - nums[1]
    nums.append(sum)
    print(nums[2])
if option == "3":
    num1 = int(input("1"))
    num2 = int(input("2 "))
    nums.append(num1)
    nums.append(num2)
    sum = nums[0] * nums[1]
    nums.append(sum)
    print(nums[2])
if option == "4":
    num1 = int(input("1"))
    num2 = int(input("2 "))
    nums.append(num1)
    nums.append(num2)
    sum = nums[0] / nums[1]
    nums.append(sum)
    print(nums[2])


""" 

"""

