import sys

treasure = 0
cheat = ("You cheated. You are dead!!!")
#start
print("Welcome my dear friend. Are you ready to go on an epic adventure?") 
start = input("With lots of treasures, evil creatures and unexpected traps? (yes / no) ")  
if start == "yes":
    print("So you are braver than I am. One piece of advice I will give to you. Decide carefully what you want to do. \nOnce you made a decision you can not change your mind and have to go one no matter how much you will regret it later on. \nBut first of all, you will need a dice. \nGo on, get one. But only one with 6 sides. No les, no more. \nCheating will be punished.")
    #first decision: Well
    print("+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x")
    print("It is a beautiful and sunny day. You are quite thirsty by now. You see a well.") 
    well = input("What do you do?  (drink / ignore) ")
    if well == "drink":
        print("You pull up the bucket of water to drink and refresh yourself. At the bottom you see something shiny. It is a golden ring.")
        treasure += 10
    else:
        print("Because you are afraid of getting poisend, you leave the well behind. Better endure a bit of thirst than getting poisend.")
    #second decision: Leprechaun
    print("You wander on. You are in a lovely green meadow. Here and there are some birches and small bushes. Suddenly you see an old odd looking tree trunk. It looks like someone lives in it. You get curiouse.") 
    trunk = input ("Do you take a look inside? (yes / no) ")
    if trunk == "yes":
        print("You see a leprechaun sitting at a table, having a cup of tea. behind him is a huge pile of gold.")
        gnome = input ("Do you fight him or do you leave? (fight / leave) ")
        if gnome == "fight":
            print("You have to roll the dice")
            score_1 = int(input("What is your score? "))
            if (score_1 % 2 == 0 and score_1 <= 6):
                print("You win 100 gold.")
                treasure += 100
            elif (score_1 % 2 != 0 and score_1 <= 6):
                print("You lost! The Leprechaun uses his magic and turns you into a bush.")
                sys.exit()
            else:
                print(cheat)
                sys.exit()
        else:
            print("You quietly leave this place and hope to get away save.")
    print("+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x")
    print("You wander on and will soon find yourself at a crossroad.")
    crossroad_1 = input ("Which way do you take? (left / right) ")
    if crossroad_1 == "right":
        print("On your way to your next adventure you suddenly find yourself in a small gorge. The way is getting more and more narrow. Listen! Can you hear that strange sound? \nAlarmed you look up but it is allready to late. Stones beginn to rain down on you. Hastely you try to take cover but a large rock hits you at the head. Everything is getting dark around you. ")
        sys.exit()
    else:
        print("On your way to your next adventure you suddenly find yourself in a small gorge. The way is getting more and more narrow. Slightly hidden behind a stone you find the entrance of a cave.")
        cave = input("Do you dare to go in? (enter / leave) ")
        if cave == "enter":
            print("The unsteady flame of your torch sheds it's light on two passages build in the massive stone. You get a bit uncomfortable in fact of the tons and tons of stone surrounding you.")
            crossroad_2 = input("Despite your feelings you decide to go on. (left / right) ")
            if crossroad_2 == "right":
                print("In the next room you enter you find a pile of 50 pieces gold")
                treasure += 50
            else:
                print("In the next room you find a strange looking creature. It seems to be some kind of rodent. But in stead of paws there are big mallets. The creature doesn't seam to realise you. \nAfter observing it quite a while you deside to venture on. But suddenly something glittering caught your eye. Next to the rat are somme gold coins. Moving towards them the rat also moves. It seems to guard them. ")
                rat = input("What do you do? (fight / leave) ")   
                if rat == "fight":
                    print("You have to roll the dice")
                    score_2 = int(input("What is your score? "))
                    if (score_2 != 6):
                        print("You win 100 gold.")
                        treasure += 20
                    elif (score_2 == 6):
                        print("You lost! The rat uses your mallets to beat you up.")
                        sys.exit()
                    else:
                        print(cheat)
                        sys.exit()
                else:
                    print("You leave the gold and move on.") 
        
        else:
            print("The path is getting even smaller")
    print("After lots of twists and turns you find yourself on a stoney plateau.")
    

else:
    print("You are as cowardly as I am. You love to read about adventures but if it is your turn to go out and be brave, you decide to stay at home and read of other peoples adventures. ")