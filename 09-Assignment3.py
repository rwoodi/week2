# Take input from user

# Is it the weekend

Sat = "Saturday"
Sun = "Sunday"
dDay = int(20)
Day = input("What is the day today? ")

if (Day == Sat):
    dDay = int(10)

if (Day == Sun):
    dDay = int(10)

# if (dDay != 10):
#    print("It is Still a Weekday, Sorry.")

if (dDay == 10):
    print("It is the Weekend, Party!")
else:
    print("It is Still a Weekday, Sorry.")

# A second method

x = input("Enter day of week: ")

if (x == "Mon"):
    print("Not a weekend")
elif (x == "Tue"):
    print("Not a weekend")
elif (x == "Wed"):
    print("Not a weekend")
elif (x == "Thu"):
    print("Not a weekend")
elif (x == "Fri"):
    print("Not a weekend")
elif (x == "Sat"):
    print("Not a weekend")
elif (x == "Sun"):
    print("Not a weekend")
else:
    print("Input Unrecognised")

# Another Method

if (( x== "Sat") or (x == "Sun")):
    print("It is Weekend")
else:
    print("Not a Weekend")