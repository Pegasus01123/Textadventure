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
    print("You wander on. you are in a lovely green meadow. Here and there are some birches and small bushes. Suddenly you see an old odd looking tree trunk. It looks like someone lives in it. You get curious.") 
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
    crossroad = input ("Which way do you take? (left / right)")
    if crossroad == "right":
        print("You find yourself in a very narrow and steep george. Suddenly you hear a loud rumbeling noise and somme small stones fall down. You take cover but the next stone that tumbles down the steep walls is fare bigger than the ones before. Your hideout is not big enough to give you shelter. \nMore and more stones are raining down. It becomes a real avalanche. A big stone hits you at your head. You die.")
    if crossroad == "left":
        print("")

else:
    print("You are as cowardly as I am. You love to read about adventures but if it is your turn to go out and be brave, you decide to stay at home and read of other peoples adventures. ")