# Check UN & PW allow 3 attempts

uN1 = "BasilB"
pW1 = "BadBunny!"
n = 3

while n > 0:
    uN1in = input("Enter Username: ")
    pW1in = input("Enter Password: ")

    if ((uN1 == uN1in) and (pW1 == pW1in)):
        print("")
        print("Username Accepted:",uN1,"Welcome to SYSTEM #")
        break # has the same results of decrementing "n" to 0
        # n = 0
    else:
        print("Credentials Rejected!")
        n = n - 1 # n -=n
        print("You have", n, "Attempts Remaining")