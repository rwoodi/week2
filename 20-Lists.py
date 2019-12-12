u1 = ["BasilB", "BadBunny!", 15000]

for i in u1:
    # print(i)
    if (i == "BadBunny!"):
        print("Found the Password for BasilB!", "It is:",i)


print("")


print(u1)
print(u1[0])
print(u1[1])
print(u1[2])
print("")

u1.remove('BasilB')
print("Remove 'BasilB' from any position")
print(u1)
print("")


u1.insert(0,'NewBasil')
print("Insert 'NewBasil' in Position 0")
print(u1)
print("")

u1.pop(2)
print("Remove value in position 2")
print(u1)
print("")

