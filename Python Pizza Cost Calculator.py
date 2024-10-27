# Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.
#
# Based on a user's order, work out their final bill. Use the input() function to get a user's preferences and then add up the total for their order and tell them how much they have to pay.
#
# Small pizza (S): $15
#
# Medium pizza (M): $20
#
# Large pizza (L): $25
#
# Add pepperoni for small pizza (Y or N): +$2
#
# Add pepperoni for medium or large pizza (Y or N): +$3
#
# Add extra cheese for any size pizza (Y or N): +$1

print("Welcome to Python Pizza!")
cost =0
while cost<1:
    size = input("What size pizza do you want? S, M or L? ").upper()
    if size=="S":
        cost+=15
    elif size=="M":
        cost +=20
    elif size=="L":
        cost+=25
    else:
        print("Please check your input")
x=0
while x==0:
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
    if pepperoni=="Y":
        if size =="S":
            cost+=2
        else:
            cost+=3
        x+=1
    elif pepperoni=="N":
        cost+=0
        x+=1
    else:
        print("Please check your input")
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese=="Y":
    cost+=1
print(f"Your final bill is: ${cost}.")
