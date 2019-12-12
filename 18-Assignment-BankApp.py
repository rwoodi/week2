# Banking Appliaction

# 1 USer - uN, Pwd, balance

# Define function
    # transfer
    # balance
    # add funds
    # userLoggenIn

# Make transfers between the 3 users

u1 = "BasilB"
u2 = "Robert"
p1 = "BadBunny!"
p2 = "password"
b1 = int(10000)
b2 = int(20000)

def logUserIn(uN, pW, euN, epW):
    if (uN == euN) and (pW == epW):
        print("User ", uN, " signed in")
        #print("So now the user can perform the actions")
        print("")
        return "Success"
    else:
        return "Failure"

i = 3
while i > 0 :
    x = input("Enter UName: ")
    y = input("Enter Pswd: ")

    if logUserIn(x, y, u1, p1) == "Success":
        break
    elif logUserIn(x, y, u2, p2) == "Success":
        break
    elif logUserIn(x, y, u3, p3) == "Success":
        break
    else:
        print("Unable to sign user ", x)
        i -= 1
        print("You have ", i, " left")

v=10
while (v ==10 ):
    Trans = input("Select Transaction:\nBal - Check Account Balance\nAdd - Add Funds to Account \nTran - Transfer Funds\nExit - Exit Menue and Logout")
    if (Trans == "Bal"):
        print("Current Balance: ",b1)
    elif (Trans == "Add"):
        amt = int(input("Amount? "))
        print("Previous Balance: ", b1)
        b1 = b1 + amt
        print("New Balance: ", b1)
    elif (Trans == "Exit"):
        print("User Requested Exit. Connection Terminated")
        v = 1
    else:
        print("Invalid Selection. User Connection Terminated")

