# JA, Conditional notes

# conditional

time = 1416
day = "tuesday"

if time < 1200 and time > 500:
    print ("good morning")
elif time < 1700:
    print("Good Afternoon")
    if day != "saturday" and day != "Sunday":
        print ("How has school been.")

elif time < 2000:
    print("Good Evening")
else:
    print("Good Night")