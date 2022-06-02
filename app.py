import random
start = True
while start:
    choices = ["R", "P", "S"]
    Player = ""
    while Player not in choices:
        Player = input("choose R,P or S:").capitalize()
    CPU = random.choice(choices)
    if CPU == Player :
        print('Player:'+"("+Player+")"+" CPU:"+"("+CPU+")"+"\nThere is a TIE")
    elif CPU == "R":
        if Player == "S":
            print('Player:'+"("+Player+")"+" CPU:"+"("+CPU+")"+"\n CPU won")
        if Player == "P": 
            print('Player:'+"("+Player+")"+" CPU:"+"("+CPU+")"+"\n Player Won")
    elif CPU == "P":
        if Player == "R":
            print('Player:'+"("+Player+")"+" CPU:"+"("+CPU+")"+"\n CPU won")
        if Player == "S":
            print('Player:'+"("+Player+")"+" CPU:"+"("+CPU+")"+"\n Player won")
    elif CPU == "S":
        if Player == "P":
            print('Player:'+"("+Player+")"+" CPU:"+"("+CPU+")"+"\n CPU won")
        if Player == "R":
            print('Player:'+"("+Player+")"+" CPU:"+"("+CPU+")"+"\n Player won")
    
    try_again = input("Would You Like To Play Again ?, select 'y' for 'Yes' and 'n' for 'No':")
    if try_again == "n" or  try_again == "N":
        break
   
     
print("Thanks For Playing")
