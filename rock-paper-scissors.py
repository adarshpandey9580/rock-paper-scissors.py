import random 
while True:
    print("\n")
    print("1) rock")
    print("2) paper")
    print("3) scissors")
    selection=int(input("enter throw:"))
    
    if (selection==1):
        player_throw="rock"
    elif (selection==2):
        player_throw="paper"    
    else:
        player_throw="scissors"
    print("\n")    
    print("player throws:",player_throw)
    throws = ("rock","paper","scissors")
    
    g_throw=random.choice(throws)

    print("g_throws:",g_throw)
    
    if (player_throw==g_throw):
        print("Tie Game")
    elif (player_throw=="rock"):
        if(g_throw=="paper"):
             print("g_wins")
        elif (g_throw == "scissors"):
            print("player wins!")
    elif (player_throw == "paper"):
        if(g_throw == "scissors"):
            print("g_wins!")
        elif(g_throw == "rock"):
            print("player wins!")
    elif (player_throw == "scissors"):
        if(g_throw == "rock"):
             print("g_wins!")
        elif(g_throw == "paper"):
            print("player wins!")       

    print("\n")
    print("1) play again")
    print("2) exit")    
    
    selection = int(input("enter choice:"))

    if (selection == 2):
        break
