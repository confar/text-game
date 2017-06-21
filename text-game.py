from sys import exit
key = False

def key_obtained():
    global key
    key = True

def begin():
    print "Let me, the author, introduce you with yourself. Are you feeling something in particular?"

    choice = raw_input("What shall it be - yes or no?\n")

    if "yes" in choice:
        print "Very good, a friend of mine. Now let's proceed to the forest"
        forest()
    else:
        bad("If you dont search into yourself, you will never find it. Goodbye.")

def forest():
    print "You are alone in the forest. A gloomy figure approaches. Do you hug it or run?"
    choice = raw_input('> ')
    if "hug" in choice:
        print "You are a brave little man. But i must warn you that in this story the author made you 10 years old. Take that into consideration when the game wants your answer. For now, you hugged the figure and it takes you on a journey"
        two_ways()
    elif "run" in choice:
        print "You decided to run and hide beneath one of the rocks. Soon you realise that the gloomy figure is being followed by a strange bird. Later you see that it is unnoticed. However you feel a little guilt when thinking of that."
        two_ways()
    else:
        bad("If you are not following the rules of the game, it punishes you with bad joke.")

def two_ways():
    print "You have a choice. There are two houses in front of you - red and black one"
    print "Which one do you take?"

    choice = raw_input("> ")

    if "black" in choice:
        black_house()
    elif "red" in choice:
        red_house()
    else:
        bad("The world does not understand your ways. You die.")

def bad(why):
    print why, "You kinda bad"
    exit(0)

def black_house():
    print "\n\nInside the black house you find yourself. There is a small boy in the room, his face is covered with a cape. He asks you a question"
    print """
    Who makes it, has no need of it.
    Who buys it, has no use for it.
    Who uses it can neither see nor feel it.
    What is it?
    """
    while True:
        answer = raw_input("> ")

        if answer == "coffin":
            print answer + " is a good try. The boy gives you a strange key"
            key_obtained()
            decision_making()
        else:
            stay = raw_input("You a wrong and can try again. Or you can go to another house. Try again?\n")
            if "yes" in stay:
                print "So what's the answer?"
            else:
                red_house()


def decision_making():
    print "You can go to another house."
    choice = raw_input("> ")
    if "go" in choice:
        red_house()
    else:
        bad("You die.")

def red_house():
    print "\n\nYou find yourself in a red house"
    print "There is a door right in front of you and it requires a key. What do you do?"
    door_is_open = False
    while True:
        choice = raw_input ("> ")
        if "open" in choice and key == True:
            print "The door is open now. You can go through it!"
            door_is_open = True
        elif "go" in choice and key == True:
            exited()
        else:
            stay = raw_input("You can return back to black house. Would you like to?\n")
            if "yes" or "yea" or "y" in stay:
                black_house()
            else:
                pass

def exited():
    print "You've done it bro! Well played!"
    exit(0)


begin()
