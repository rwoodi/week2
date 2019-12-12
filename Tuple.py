# a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

thistuple = ("apple", "banana", "cherry", "orange")
print(thistuple)

print(thistuple[0])
print(thistuple[1])
print(thistuple[2])
print(thistuple[3])

print("\nNegative Tuple")
print(thistuple[-1])
print(thistuple[-2])
print(thistuple[-3])
print(thistuple[0]) # This one is not negative, but does put the first item in last position

print(thistuple[0 : 4])