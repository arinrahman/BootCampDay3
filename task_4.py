#more complex nested if

print("Welcome to Luna Park! Excited for a rollercoaster ride?")
age= int(input("How old are you?\n"))
h=float(input("Please enter your height in cm to check eligibility for this ride.\n"))
if h>120:

    if age < 12:
        cost= 5

    elif age >= 12 and age <=18:
        cost = 7


    else:
        cost=12
    print(f"Pay ${cost} for a fun rollercoaster ride!")

else:
    print("Sorry, you can't ride. You need to grow taller to ride the rollercoaster.")