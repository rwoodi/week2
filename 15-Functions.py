def myFunA():
    print(" -" * 50)
    print("This is my Function A")
    print(" -" * 50)

def myFunB(val1, val2):
    print(" -" * 50)
    print("This is my Function B")
    print(val1, val2)
    print(" -" * 50)

myFunA() # Calls the funtion
myFunB(10, "234234")# Allowing Input for val1 and val2 as 10, 234234

def myFunC(X, Y):
    z = (X + Y)/2
    return z

print(myFunC(20,50))

a = myFunC(40, 35)
print(a)
