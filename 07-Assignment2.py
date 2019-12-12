# Create a UName and PWd in the code

# Collect credentials from user input

# Match to see if credentials are correct

UName = "BasilB"
Pwd = "BadBunny!"

UNameInput = (input("Enter Username: "))
PwdInput = (input("Enter Password: "))

print(UNameInput)
print(PwdInput)

matchUN = (UName == UNameInput)
matchPwd = (Pwd == PwdInput)

print("Username Match: ",matchUN)
print("Password Match: ",matchPwd)

if (UName == UNameInput) :
    print("Username Match")
else:
    print("Username Does not Match")

if (Pwd == PwdInput):
        print("Password Match")
else:
        print("Password Does not Match")

