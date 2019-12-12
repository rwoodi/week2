s1 = "Welcome to the team PSE"

s2 = "Lets Python!!!"

print(s1)
print(type(s1))

print("The length of the string is ", len(s1))

print(s1[0])
print(s1[22])

print("End of my program")

print(s2.upper())
print(s2.lower())

if (s2.isupper()):
    print("YES they are upper case")
else:
    print("NOPE. NOT UPPER.")


print(s1.strip()) # Strip Takes away extra spaces

print("Position of ! in s2 is at ",s2.index("!!!"))

# print(s2.replace("!!!","@@@"))

print("End of my program")