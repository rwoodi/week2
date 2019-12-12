for I in range(10) : # Creates variable I, start with 0, go till I < 10 true
    print("Bob")
    print(I)

print("-----------------------------")

k = 0
s1 = "Sun and the Moon"
for s2 in s1:
    # print(k+1, s2) # S2 Prints the position Number ans character in s1.  Modified to stat position at 1 as opposed to 0
    print(s2," is in position ", k, " and is character ", k+1)  # S2 Prints the position Number ans character in s1.  Modified to stat position at 1 as opposed to 0
    k = k + 1 # This logic will count the blank spaces as well

print("-----------------------------")

print(s2[0]) # Print value of s2 in position 0
# print(s2[1]) # Print value of s2 in position 1, Nothing in this position
print(s1[0])

print("End")
