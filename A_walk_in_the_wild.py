import sys

treasure = 0
cheat = ("You cheated. You are dead!!!")
#start
print("Welcome my dear friend. Are you ready to go on an epic adventure?") 
start = input("With lots of treasures, evil creatures and unexpected traps? (yes / no) ")  
if start == "yes":
    print("So you are braver than I am. One piece of advice I will give to you. Decide carefully what you want to do. \nOnce you made a decision you can not change your mind and have to go on no matter how much you will regret it later on. \nBut first of all, you will need a dice. \nGo on, get one. But only one with 6 sides. No less, no more. \nCheating will be punished.")
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

    print("You wander on. You are in a lovely green meadow. Here and there are some birches and small bushes. Suddenly you see an  odd looking old tree trunk. It looks like someone lives in it. You get curiouse.") 

    trunk = input ("Do you take a look inside? (yes / no) ")
    if trunk == "yes":
        print("You see a leprechaun sitting at a table, having a cup of tea. Behind him is a huge pile of gold.")
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
    #crossroad
    print("You wander on and will soon find yourself at a crossroad.")

    crossroad_1 = input ("Which way do you take? (left / right) ")
    if crossroad_1 == "right":
        print("On your way to your next adventure you suddenly find yourself in a small gorge. The way is getting more and more narrow. Listen! Can you hear that strange sound? \nAlarmed you look up but it is allready to late. Stones beginn to rain down on you. Hastely you try to take cover but a large rock hits you at the head. Everything is getting dark around you. ")
        sys.exit()
    else:
        print("On your way to your next adventure you suddenly find yourself in a small gorge. The way is getting more and more narrow. Slightly hidden behind a stone you find the entrance of a cave.")
        #cave
        cave_1 = input("Do you dare to go in? (enter / leave) ")
        if cave_1 == "enter":
            print("The unsteady flame of your torch sheds its light on two passages build in the massive stone. You get a bit uncomfortable due to the tons and tons of stone surrounding you.")
            #crossroad
            crossroad_2 = input("Despite your feelings you decide to go on. (left / right) ")
            if crossroad_2 == "right":
                print("In the next room you enter you find a pile of 50 pieces of gold")
                treasure += 50
            else:
                #rat with mallets
                print("In the next room you find a strange looking creature. It seems to be some kind of rodent. But in stead of paws there are big mallets. The creature doesn't seam to realise you entered the cave. \nAfter observing it for quite a while you deside to venture on. But suddenly something glittering caught your eye. Next to the rat are some gold coins. Moving towards them the rat also moves. It seems to guard them. ")
                rat = input("What do you do? (fight / leave) ")   
                if rat == "fight":
                    print("You have to roll the dice")
                    score_2 = int(input("What is your score? "))
                    if (score_2 != 6):
                        print("You win 100 gold.")
                        treasure += 100
                    elif (score_2 == 6):
                        print("You lost! The rat uses its mallets to beat you up.")
                        sys.exit()
                    else:
                        print(cheat)
                        sys.exit()
                else:
                    print("You leave the gold and move on.") 
        
        else:
            print("The path is getting even smaller")
    print("After lots of twists and turns you find yourself on a stoney plateau. It's dark and foggy.\nThere is an old signpost with three arms laying on the ground. One of the signs states 'Danger'. But which way was meant?")
    #crossroad
    crossroad_3 = input("Which way do you take? (straight / left / right) ")
    if crossroad_3 == "left":
        #cave with minotaur
        print("After some time walking in a foggy night you find yourself yet in an other cave. But this time you see a red light shining in front of you.")
        cave_2 = input("In front of you are two ways similar lit by this gloomy red light. One leads down, one to the left. (down / left) ")
        if cave_2 == "left":
            print("You start walking. It's getting warmer and warmer. The light is getting more and more intense. Suddenly there is a sharp bent. Carefully you take a step round the corner.\nYou find yourself in a hugh cave. Its inhabitant is a tremendously big what? A Bull, a minotour? You are not sure about it. \nBut the nature of the creature is not your biggest problem as it starts walking up to you dragging a big whip behind him.\nSuddenly a big stone crashes down behind you blocking your retreat. You have to fight. ")
            print("You roll the dice.")
            score_3 = int(input("What is your score? "))
            if (score_3 == 6 or score_3 == 1):
                print("You win 1000 gold.")
                treasure += 1000
            elif (score_3 != 6 or score_3 != 1):
                print("You lost! The minotaur uses its whip to rip the flesh of your bones.")
                sys.exit()
            else:
                print(cheat)
                sys.exit()
        else:
            print("You start walking downwards. It's getting warmer and warmer. The light is getting more and more intense. Suddenly there is a sharp bent. Carefully you take a step round the corner. \nSadly you haven't been carefull enough. Your next step will only find thin air. Falling you see a sea of lava underneath.")
            sys.exit()
    elif crossroad_3 == "right":
        #Sea with octopus
        print("Slowly but surely the fog lifts. the path you took leads you gently downwards to a big lake. Far of the lakeside you can see a small island. Somehow you know you will find a treasure at the Island. But how do you get there? ")
        sea = input("You could try to swim or search for some kind of boat. (swim / search) ")
        if sea == "swim":
            print("Because the weather is nice and warm you decide to swim. But after around half the way you feel something toutching your ankle. Looking down you see a creature that would be fascinating to watch out of a save boat. \nBut because you haven't got a boat it is terrifing. Looking like an octopus made out of jelly. Slimy but still solid. It wraps its tentacle round your feet and tries to pull you down. You have to fight it. ")
            print("You roll the dice.")
            score_4 = int(input("What is your score? "))
            if (score_4 % 2 != 0 and score_4 <= 6):
                print("You win 300 gold.")
                treasure += 300
            elif (score_4 % 2 == 0 and score_4 <= 6):
                print("You lost! The slimy octopus hugs you and pulls you under water.")
                sys.exit()
            else:
                print(cheat)
                sys.exit()
        else:
            print("Hidden in the reed you find an old rusty tub. You decide to use this thing to get to the island without getting wet. A young tree has to work as oar.\nWhile you are on your way to the island you see something strange swimming underneath your boat. It looks a bit like an octopus but less solid more like a jellyfish in the shape of an octopus. \nFinally you arrive at the island. And indeed, in the middle of the island you find a chest with gold.")
            treasure += 50
        
    else:
        print("You choose to walk straight on. The fog is getting thicker and thicker. Suddenly the sound of your steps changes. First you were walking on a massive stone plateau but suddenly there are small stones under your feet. With your next step the stones begin to move. You stumble. Trying to find your balance you take a step to the side but instead of a ground you find yourself stepping into thin air.")
        sys.exit()

    print(f"After all this adventures you decide to take a rest. You find a nice looking guesthouse and rent a small room. After refreshing yourself you count the gold you discovered. \nOn your adventures you found {treasure} gold.")
else:
    print("You are as cowardly as I am. You love to read about adventures but if it is your turn to go out and be brave, you decide to stay at home and read of other peoples adventures. ")