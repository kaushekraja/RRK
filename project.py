
import random
choices=["rock","nuke","bomb"]
computer=(random.choice(choices))
player_points=0
System_points=0
while True:
    player=input("rock or,nuke,bomb?")
    if player == computer:
          print("tie")
    elif player == "bomb":
         if computer == "rock":
             print("you win","player","demolish","computer")
             player_point+=1
         if computer == "nuke":
            print("you lose",computer,"destroy",player)
            System_points+=1
    elif player == "nuke":
         if computer == "rock":
             print("you win",player,"explodes",computer)
             player_point+=1
         if computer == "nuke":
            print("you lose",computer,"destroy",player)
            System_points+=1
    elif player == "rock":
         if computer == "nuke":
             print("you lose",computer,"demolish",player)
             System_points+=1
         if computer == "bomb":
            print("you win",player,"pushes",computer)
            player_points+=1

    else:
        print(player_points)
        print(System_points)
        break