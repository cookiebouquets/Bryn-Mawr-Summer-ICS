""" 
We're going to create a bank program for the rest of class

    1) We can create new accounts
    2) We can close accounts
    3) Withdraw money
    4) deposit money
    5) Transfer money

Our objective is to create a function for each of these behaviors and then string them all together as one final program inside
of a def main() function 
"""

"""
You want to do all of your data collection inside of def main()? 

Create account is going to update our dictionary with the account and values specified inside of def main 
    - We need to collect account name and balance before even calling createAccount()
    - We need to determine what our list of parameters
    - functions don't know things outside of themselves, we need to inform the functions with the data that matters 
"""

def createAccount(name,balance,accts):
    accts[name] = balance #This is how we added things to dictionaries

def closeAccount(name,accts):
    if name in accts.keys(): #This will search the list of keys for our dictionary and check to see if name is inside 
        accts.pop(name)
    else:
        print("That is not a valid account name")

def withdraw(name,amount,accts): #Not only performing its functionality, but also returing a boolean value for a (un)successful operation
    if name in accts.keys():
        if amount > accts[name]:
            print("amount exceeds account balance")
            return False
        else:
            accts[name] = accts[name] - amount
            return True
    else:
        print("That is not a valid account name")
        return False 

def deposit(name,amount,accts):
    if name in accts.keys():
        accts[name] = accts[name] + amount
    else:
        print("That is not a valid account name")

def transfer(acct1,acct2,amount,accts):
    if acct1 in accts.keys() and acct2 in accts.keys():
        if withdraw(acct1,amount,accts) == True:
            deposit(acct2,amount,accts)
        
    else:
        print("One of those accounts is not a valid account")
        print("Accounts not updated")

def printAccounts(accts):
    print("----- Accounts -----")
    for name in accts:
        print(f"Account name: {name}    Balance: {accts[name]}")

def main():
    accounts = {"John Pork":500.0}
    check = True
    while check == True:
        print("Welcome to the Bank!")
        print("1. Create Account")
        print("2. Close Account")
        print("3. Withdraw")
        print("4. Deposit")
        print("5. Transfer")
        print("6. Quit")
        option = input("Enter your option from the list above: ")
        if option.isnumeric() == True:
            if int(option) == 1:
                printAccounts(accounts)
                acctname = input("Enter the name of your account: ").strip()
                balance = float(input("Enter your balance: "))
                createAccount(acctname,balance,accounts)
                printAccounts(accounts)
            elif int(option) == 2:
                printAccounts(accounts)
                acctname = input("Enter the name of the account you wish to close: ").strip()
                closeAccount(acctname,accounts)
                printAccounts(accounts)
            elif int(option) == 3:
                printAccounts(accounts)
                acctname = input("Enter the account name you wish to withdraw from: ").strip()
                amt = float(input("Enter the Amount you wish to withdraw: "))
                withdraw(acctname,amt,accounts)
                printAccounts(accounts)
            elif int(option) == 4:
                printAccounts(accounts)
                acctname = input("Enter the account name you wish to deposit to: ").strip()
                amt = float(input("Enter the Amount you wish to deposit: "))
                deposit(acctname,amt,accounts)
                printAccounts(accounts)
            elif int(option) == 5:
                printAccounts(accounts)
                acct1 = input("Enter the account name you wish to transfer from: ").strip()
                acct2 = input("Enter the account name you wish to transfer to: ").strip()
                amt = float(input("Enter the Amount you wish to transfer: "))
                transfer(acct1,acct2,amt,accounts)
                printAccounts(accounts)
            elif int(option) == 6:
                print("Thanks for visiting!")
                check = False
        else:
            print("Invalid input")

main()

""" 
So we got the basic functionality of our program working. But it's a really fragile program: 
    - if we don't type in the exact data types the program is expecting, it'll crash 
    - if we don't type in the exact strings the program is expecting, it'll crash

    "John Pork "

    -First thing we can fix is verifying whether or not the things we type in are actually accounts
    -With while loops, wait until the user types in a valid account name
        -If they don't loop back to the start
        -If they do, let them do their function
    OR
    -inside each function, we check to see if its a valid account, if it's not, then we just print "invalid account"

    We fixed the string errors, we need to fix the type checking errors next. 

    10:20

When we type in an option that isn't a number, then the program shuts down and we have to restart. We need some way to check if option is actually a number
The good news is: 
    - There's actually a string function that checks if the string is a numeric value. 

Anytime we change our program to fix a bug
    - Refactoring our code. 

    We changed the moment from which we typecasted. Originally we typecasted immediately after calling input() but we want access to the string functions before we 
    do any checking for what option actually is. So instead we typecast in our if-elif-else chain instead of where input is.

    isnumeric() returns true if the string looks a number and returns false if there are anything non-number related in the string

So we've fixed most if not all of our possible type errors/typo errors that will end up crashing the program. All that's left is 
making our output look nicer and also making sure we don't have any overdrafts on accounts 
"""