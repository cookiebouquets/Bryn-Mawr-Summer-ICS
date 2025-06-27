"""
So today we're going to cover number systems

we're going to start with base-10 first (decimal) then we're going to move onto binary
base-2) and the last thing we're going to cover is Hexadecimal (base-16)

First we're going to talk about decimal.

We have 10 digits: 0-9 When we hit 10, counting starts over 

10 is the "rollover point" for the position of a number

99 => 100 999 => 1000

The anatomy of a number: We can really break down base-10 numbers into exponents of 10


572 = 5 * 10^2 + 7 * 10^1 + 2 * 10^0
So each position i.e. 500, 70, 2 are all powers of 10. 

1 = 10^0
10 = 10^1
100 = 10^2
1000 = 10^3

Adding up combinations of powers of 10 gives you every number in base-10. 

Binary is the same thing but instead of powers of 10, we're working with powers of 2
So if we're working over powers of 2, our digits are the numbers 0 and 1.

1101 <= Binary number, 0s and 1s

1*2^3 + 1*2^2 + 0*2^1 + 1*2^0 = 8 + 4 + 1 == 13  

So why binary in particular? This is really an electrical engineering problem. We're working 
with technology from the 1930s-1950s. We're working with mostly vaccuum as our way to manipulate
electrical charges. These things are huge. We have 2 state we want to distinguish: 

HIGH and LOW. <= Usually requires three pieces of measuring equipment 

The equipment sucked and also it was too big to use. 

Bit = an individual 1 or 0
Byte = A collection of 8 Bits

1111 1111 <= This is a byte 

What's the largest number we can store in a byte? 255

How do we count in binary:
0000 = 0
0001 = 1
0010 = 2
0011 = 3
0100 = 4
0101 = 5
0110 = 6
0111 = 7 
1000 = 8 <= if you fill this in this should go up to the number 15

How do we convert from Decimal to Binary? We need to do modular arithmetic for this task

115 <= I want to convert this into binary

I want to divide 115 by 2 until I can no longer divide by 2. I also want to keep track
of the remainders 

115 % 2 = 57 R 1
57 % 2 = 28 R 1
28 % 2 = 14 R 0
14 % 2 = 7 R 0
7 % 2 = 3 R 1
3 %2 = 1 R 1
1 % 2 = 0 R 1

So now I have a list of remainders from top to bottom. Now to get my binary number I rewrite
my remainders from left to right going up the list. 

1110011 <= 115 in binary


1 x 2^6 + 1*2^5 + 1*2^4 + 0 *2^3 + 0*2^2 + 1 *2^1 + 1*2^0 
    64    +    32  +      16   +     0   +     0   +   2    +  1 = 115


Convert these numbers from decimal to binary: 

 93 = 1011101
 20 = 10100

 20 % 2 = 10 R 0
 10 %2 = 5 R 0
 5 %2 = 2 R 1
 2 % 2 = 1 R 0
 1 % 2 = 0 R 1

 10100
 

 72 = 1001000
 94 = 1011110

94 % 2 = 47 R 0
47 %2 = 23 R 1
23 %2 = 11 R 1
11 %2 = 5 R 1
5 % 2 = 2 R 1
2 % 2 = 1 R 0
1 % 2 = 0 R 1

 89 = 1011001

Convert these binary numbers from Binary to Decimal: 

1011 1101 = 189
1101 0011 = 211
1001 1101 = 157
0110 1011 = 107

1 * 2^0 + 1 *2^1 + 0 *2^2 + 1*2^3 + 0*2^4 + 1*2^5 + 1*2^6 + 0*2^7
1 + 2 + 0 + 8 + 32 + 64 = 107


9:25

What I've covered so far: 

Binary to Decimal
Decimal to Binary 
A historical lesson

What distinguishes binary from decimal is how easy it is to do math with them 

five operations
    - addition
    - subtraction
    - AND
    - OR
    - XOR

addition and subtraction work exactly the same way they do in decimal (with some caveats)

0 + 0 = 0
1 + 0 = 1
0 + 1 = 1
1 + 1 = 10
 11111 11 
  10111001
+ 11001011
__________
 110000100

Subtraction: Also works pretty in the same way

0 - 0 = 0
1 - 0 = 1
1 - 1 = 0
0 - 1 = 1 (With a borrow from the position to the left)

  /1 
 110
-101
____
 001

 110 = 6
 101 = 5
6 - 5 = 1 


10
01
__
01

2^1 - 2^0 = 2 - 1 = 1 == 2^0 

2^2 - 2^1 = 4 - 2 == 2 <=> 2^-1

0100 <= 2^2
0010 <= 2^1
0010 <= 2^1

Addition and subtraction are not a good representation as to why binary is ubiquitous in 
computer science. Operations in computer science are done bitwise 

bitwise = operation is evaluated bit by bit from left to right

1 0 0 1 1 1 1
1 0 1 0 1 1 0

Examples of bitwise operations:

AND OR and XOR

we've seen AND and OR before: when we were evaluating boolean sentences

if x < 5 and check == true <= for this to evaluate to True, BOTH conditions had to be true
    1   AND   1  == TRUE

ORs: 

if x < 5 OR check == True <= for this to evaluate to true, either sentence must be correct
(inclusive if both are true)

x = 4 
check = False 
s = True

x = 6
check = True
s = true

x = 4 
check = True
s = true

Truth for AND: a AND b = 1 or 0

1 AND 1 = 1
1 AND 0 = 0
0 AND 1 = 0
0 AND 0 = 0




if x < 5:

x = 4 evaluates sentence 214 to 1 

if check == True

check = true evaluates sentence 218 to 1

if x < 5 AND check == True: 

if 1 AND 1 = 1:

if x < 5 AND Check = true:

x = 6 and check = False  

1 0 11100
1 1 00110
_______
1000100

^Result after performing AND bitwise on our two bitstrings 

Truth Table for OR: 

1 OR 1 = 1
1 OR 0 = 1
0 OR 1 = 1
0 OR 0 = 0 

1011100
1100110
_______
1111110

AND typically gives smaller bit strings and OR typically gives bigger bitstrings 

XOR (The same as OR, EXCEPT for the 1 XOR 1 case)
1 XOR 0 = 1
0 XOR 1 = 1
1 XOR 1 = 0
0 XOR 0 = 0

1011100
1100110
_______
0111010


So the question is: Why is XOR useful at all? XOR is called a reversible function 
x XOR y = z
y XOR z = x

1100110
0111010
_______
1011100

10:25 Hexadecimal When we come back

10111010101110101010101101101110101011 <= This sucks 

Is there a way to store the same amount of information in less digits? Yes, we can do this using hexadecimal

Hexadecimal = Base 16

There's a problem:
    Decimal = 0-9
    Binary = 0-1
    Hexadecimal = 0-15

    what happens for the numbers 10-15? We can't store that information as one character with just numbers
    We can replace 10-15 with letters

10 = A
11 = B
12 = C
13 = D
14 = E
15 = F

0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F as our possible digits in base 16 (hexadecimal)

decimal to hexadecimal <= I don't really care to see this 
Binary to Hexadecimal 

1 Byte = 8 Bits
Largest number you can store in 1 byte is 255
1 Byte = two 4 Bit register
255 = 1111 1111

1111 <= 2^0 + 2^1 + 2^2 + 2^3 = 1 + 2 + 4 + 8 = 15 is the largest number you can store in one 4 bit register

I can convert binary numbers into hexadecimal numbers by looking at 4 bit registers

1111 = 15 = F

1100 1010 1111
  C         F

1100 = 0 + 0 + 2^2 + 2^3 = 4 + 8 = 12 

1010 = 0 + 2^1 + 0 + 2^3 = 2 + 8 = 10 = A

110010101111 = CAF 

I've shown you exactly how hexadecimal numbers make storing large binary numbers easier. How is this useful in 
other domains?

RGB = red, green, blue 
    = (0-255,0-255,0-255)
    = Each color corresponds to one byte of information
    = (1010 1010, 1100 0011, 1010 0101)
    = (AA, C3, A5)
    1010 = 0 + 2 + 0 + 8 = 10 = A
    1100 = 0 + 0 + 4 + 8 = 12 = C
    0011 = 1 + 2 + 0 + 0 = 3

    1010 = A
    0101 = 1 + 0 + 4 + 0 = 5

    AAC3A5 corresponded to a weird green color. I've shown that you can take a binary number, convert it to hex
    use that hex number as a way of at a color 
"""

