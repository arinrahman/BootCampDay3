print("Welcome to Python Pizza Deliveries!")
size=input("What size pizza do you want? S, M or L?\n")
pepperoni=int(input("Do you want peperoni? 1 for Yes & 0 for No?\n"))
extra_cheese=int(input("Do you want extra cheese? 1 for Yes & 0 for No?\n"))

if size== "S":
    cost=15
elif size== "M":
    cost=20
else:
    cost=25
if pepperoni==1 and size=="S":
    cost+=2
if pepperoni==1 and (size=="M" or size== "L"):
    cost+=3
if extra_cheese==1:
    cost+=1
print(f"Your final bill is: ${cost}")



