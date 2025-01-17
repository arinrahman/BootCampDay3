#nested else if statement

print("Welcome to Luna Park! Excited for a rollercoaster ride?")
age= int(input("How old are you?\n"))
h=float(input("Please enter your height in cm to check eligibility for this ride.\n"))
if h>120:

    if age <= 18 :
        cost= 7
        print(f"Pay ${cost} for a fun rollercoaster ride!")
    else:
        cost=12
        print(f"Pay ${cost} for a fun rollercoaster ride!")

else:
    print("Sorry, you can't ride. You need to grow taller to ride the rollercoaster.")