# Print a multiplication table
# user enters the input number(n1=12) and column number(n2=3)
# Should be 10 rows
# then the print should be

n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))

v1 = 1
v2 = 11

def mYfunc ():
    for i in range(v1, n2+1):
        t= n1, '*', i, "=:", n1 * i, "\t"
    print(t)


#    if n2 > 10:
#        print("Next Level")
#        #print(n1, "multiplied by", i, "is:", n1 * i)
#    else:
#        print("Exit")

mYfunc()

"""""
for i in range(v1,v2):
    print (n1,"multiplied by", i, "is:",n1*i)
    v1=v1+1
    v2=v2+1
if n2>11:
    for x in range(v1, v2):
        print(n1, "multiplied by", x, "is:", n1 * x)
        v1 = v1 + 1
        v2 = v2 + 1
else:
    print("This is the end")
if n2 > 21:
    for x in range(v1, v2):
        print(n1, "multiplied by", x, "is:", n1 * x)
else:
    print("This is the end")

"""""

