# Scratch Code Here
"""""
for i in range(6, 10+1): # starts the counter at 6 and ends at 10 (naturally 9, but +1 makes it 10)
    print(i)

"""""
"""""
# Scratch Pad Function
def func(x, y):
    a = (x + y)/2
    return a

i1=int(input("Var 1:"))
i2=int(input("Var 2:"))

print(i1)
print(i2)
print(func(i1,i2))
"""""
"""""
print("Dog\nCat\nBird") # \n New LIne
# print("\r") # \r Carriage  Return - Will replace anything in front of it
print("\n") #\n Seems to create two spaces
print("End")

print("This is a carriage return\rCatDog")

"""""
"""""
n = "Bob"
print(n, n, n, sep='_') # The sep command defines the character the seperates variables in a print statement

# The end key of print function will set the string that needs to be appended when printing is done

# initialize a list
initList = ['camel', 'case', 'stop']

# print each words using loop
print('Printing using default print function')
for item in initList:
    print(item)  # default print function. newline is appended after each item.

print()  # another newline

# print each words using modified print function
print('Printing using modified print function')
for item in initList:
    print(item, end='-')
"""""
""""
print("twinkle, twinkle\n\tlittle star.\n\t\tWTF is wrong with you?") #\n New Line \t Tab
"""
"""
import sys

print(sys.version)
print(sys.version_info)
"""
"""
import calendar #  import all the classes of this module.
c= calendar.TextCalendar(calendar.SUNDAY) # tells the interpreter to create a text calendar. Start of the month will be Sunday.
y = int(input("Year: "))
m = int(input("Month: "))
str= c.formatmonth(y,m) # We are creating calendar for the year 2025, Month 1 – January
print (str) #print str will print the output.
"""
"""
# myF = open("C:/Users/rwoodi/PycharmProjects/untitled/MyFile") # Either Format Opens
# myF = open("C:\\Users\\rwoodi\\PycharmProjects\\untitled\\MyFile") # Either Format Opens
myF = open("I:\Python\Class2-Projects\myFile.txt")
print(myF.read())

"""

# print(0x10)

l1 = [192,168.100.1]

a = 192
b = 168
c = 1
d = 100

# print(hex(a, b, c, d))

print(a,b,c,d)
print(hex(a,b,c,d))
