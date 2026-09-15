import random  # for shuffling and events that require probability
import time  # for pacing



hand = []
stack = []
cards = ["Kiyomi: Erologist",
         "Kiyomi: Fortune Teller",
         "Kiyomi: Writer",
         "Mili: Lover",
         "Mili: Aichmophile",
         "Mili: Kura",
         "Malika: Roll",
         "Malika: Jackpot",
         "Malika: Tiandeng",
         "Kzuhr: Lost Paradise",
         "Kzuhr: Susurration",
         "Kaiin: Hide n' Seek",
         "Kaiin: Duty Calls", ]  # list of cards
sanity = 10
pity = 0

def shuffling():
    global stack, hand, cards
    for i in range(5):  # repeats this 5 times
        for card in cards:
            stack.append(card)  # adds all cards
    random.shuffle(stack)  # randomizes

number = 0
def drawing():
    global stack, hand, number
    if number >= len(stack):
        print("Game over. No more cards.")  # ending message
        quit()
    else:
        hand.append(stack[number])  # gets the next card from the stack
        number += 1


knife = "no"
def play():
    global hand, sanity, number, pity, knife
    action = input("Draw or play? (draw/play): ")

    # DRAW SECTION

    if action == "draw" and len(hand) < 5:
        drawing()
        print(hand)

    # error for when you have too many cards in your hand
    elif action == "draw" and len(hand) >= 5:
        print("You can't draw more than 5 cards!")
        action = "play"

    # PLAY SECTION

    if action == "play":

        use = int(input("Which card will you play? (1-5): "))  # asking which card the player will use

        # error for when they enter an invalid number
        if use < 1 or use > len(hand):
            print("You entered an invalid number. Try again.")
            play()

        # plays the event depending on which card they picked
        else:
            if hand[use - 1] == "Kiyomi: Erologist":
                print("K: \"What seems to be the problem?\"")
                time.sleep(2)
                print("You tell her your feelings.")
                time.sleep(2)
                vl = random.randint(1, 3)
                if vl == 1:
                    print("K: \"Take these\"")
                    time.sleep(2)
                    print("She gives you some pills.")
                elif vl == 2:
                    print("K: \"We need to give you some shots\"")
                    time.sleep(2)
                    print("She gives you a few shots.")
                elif vl == 3:
                    print("K: \"You need a few stitches\"")
                    time.sleep(2)
                    print("She stitches you up.")
                time.sleep(2)
                sanity += 3
                print("Sanity +3")
            elif hand[use - 1] == "Kiyomi: Fortune Teller":
                print("K: \"So you wanna see the future, huh?\"")
                time.sleep(2)
                if number + 3 >= len(stack):
                    print("K: \"You've reached the end of the pile. Eh, I'll give you the rest anyway.\"")
                    print(stack[number:])
                else:
                    print(stack[number:number + 3])
            elif hand[use - 1] == "Kiyomi: Writer":
                print("You chose to write your feelings down")
                time.sleep(2)
                fate = random.randint(1, 2)
                if fate == 1:
                    print("It helps cleanse your mind")
                    time.sleep(2)
                    sanity += 3
                    print("Sanity +3")
                elif fate == 2:
                    print("It makes the voices in your head louder")
                    time.sleep(2)
                    sanity -= 3
                    print("Sanity -3")
            elif hand[use - 1] == "Mili: Lover":
                print("Oh, you have fallen again.")
                time.sleep(2)
                if "Kiyomi: Erologist" in hand:
                    print("You went to the erologist.")
                    time.sleep(2)
                    fate = random.randint(1, 5)
                    if fate < 5:
                        print("It worked.")
                        time.sleep(2)
                        sanity += 5
                        print("Sanity +5")
                    elif fate == 5:
                        print("Yet she can't stitch the heart that hurts.")
                        time.sleep(2)
                        sanity -= 10
                        print("Sanity -10")

                else:
                    fate = random.randint(1, 2)
                    if fate == 1:
                        print("Love can calm.")
                        time.sleep(2)
                        sanity += 5
                        print("Sanity +5")
                    elif fate == 2:
                        print("Love can hurt.")
                        time.sleep(2)
                        sanity -= 5
                        print("Sanity -5")
            elif hand[use - 1] == "Mili: Aichmophile":
                print("Your love for blades is stronger than no other")
                time.sleep(2)
                if sanity >= 10:
                    print("\"I'm keeping this.\"")
                    time.sleep(2)
                    print("Protection Acquired.")
                    knife = "yes"
                elif sanity < 10:
                    print("You slash your own wrists.")
                    time.sleep(2)
                    sanity -= 3
                    print("Sanity -3")
            elif hand[use - 1] == "Mili: Kura":
                print("Under the sakura tree...")
                time.sleep(2)
                if "Kzuhr: Lost Paradise" in hand:
                    sanity += 10
                    print("You spot a familiar figure, the song of the past filling your heart with fullness")
                    time.sleep(2)
                    print("Sanity +10")
                else:
                    sanity += 3
                    print("You weep, remembering days of golden air.")
                    time.sleep(2)
                    print("Sanity +3")
            elif hand[use - 1] == "Malika: Roll":
                print("You roll a dice.")
                time.sleep(2)
                guess = input("Odd or even? (odd/even): ")
                roll = random.randint(1, 6)
                mod = roll % 2
                if guess == "odd" and mod == 0:
                    print("Even.")
                    sanity -= 3
                    pity += 1
                    time.sleep(2)
                    print("Sanity -3")
                elif guess == "even" and mod == 0:
                    print("Even.")
                    sanity += 3
                    time.sleep(2)
                    print("Sanity +3")
                elif guess == "odd" and mod == 1:
                    print("Odd.")
                    sanity += 3
                    time.sleep(2)
                    print("Sanity +3")
                elif guess == "even" and mod == 1:
                    print("Odd.")
                    sanity -= 3
                    pity += 1
                    time.sleep(2)
                    print("Sanity -3")
            elif hand[use - 1] == "Malika: Jackpot":
                print("Jackpot!")
                time.sleep(2)
                if pity > 0:
                    print("You've accumulated pity over the game. It has aided this turn.")
                    time.sleep(2)
                sanity += 3 + pity
                print(f"Sanity +{3 + pity}")
            elif hand[use - 1] == "Malika: Tiandeng":
                print("M: \"Oh, if only you were here to see them.\"")
                time.sleep(2)
                if sanity >= 20:
                    print("\"Best wishes, Lika\"")
                    time.sleep(2)
                    sanity += 5
                    print("Sanity +5")
                else:
                    print("Seeing your sister happy... it hurts a bit.")
                    time.sleep(2)
                    sanity -= 5
                    print("Sanity -5")
            elif hand[use - 1] == "Kzuhr: Lost Paradise":
                print("What even is a lost paradise...?")
                time.sleep(2)
                if "Mili: Kura" in hand:
                    dialogue = ["\"Zuha?\"",
                                "K: \"Yeah?\"",
                                "\"Promise we'll be friends forever and ever and ever?\"",
                                "K: \"Of course! Why wouldn't we be?\"",
                                "\"Well-\""]
                    time.sleep(2)
                    print("It's...")
                    time.sleep(2)
                    print("Your mind goes fuzzy.")
                    time.sleep(2)
                    for text in dialogue:
                        for letter in text:
                            print(letter, end="", flush=True)
                            time.sleep(.3)
                        print("")
                        time.sleep(1)
                    print("...It's a paradise. Close, but too far.")
                    time.sleep(2)
                    sanity += 5
                    print("Sanity +5")
                else:
                    print("...")
                    time.sleep(2)
                    print("Can't remember.")
                    time.sleep(2)
                    sanity -= 5
                    print("Sanity -5")
            elif hand[use - 1] == "Kzuhr: Susurration":
                print("K:\"Listen to the leaves, listen to them sing.\"")
                time.sleep(3)
                print("The susurration calms you.")
                time.sleep(2)
                sanity += 3
                print("Sanity +3")
            elif hand[use - 1] == "Kaiin: Hide n' Seek":
                print("K:\"Hehehe\"")
                time.sleep(2)
                fate = random.randint(1, 3)
                if fate < 3:
                    print("\"Found you\"")
                    time.sleep(2)
                    sanity += 3
                    print("Sanity +3")
                else:
                    print("\"Kaiin...? Kaiin??\"")
                    time.sleep(2)
                    print("You never found him.")
                    time.sleep(2)
                    sanity -= 5
                    print("Sanity -5")
            elif hand[use - 1] == "Kaiin: Duty Calls":
                print("K:\"You can handle them, right? I'll be west.\"")
                time.sleep(2)
                if knife == "yes":
                    print("Easy work.")
                    time.sleep(2)
                    sanity += 5
                    knife = "no"
                    print("Sanity +5")
                else:
                    fate = random.randint(1, 2)
                    if fate == 1:
                        print("You couldn't handle them.")
                        time.sleep(2)
                        sanity -= 5
                        print("Sanity -5")
                    else:
                        print("You were able to defeat them.")
                        time.sleep(2)
                        sanity += 3
                        print("Sanity +3")
            time.sleep(2)
            print(f"\n\nSanity: {sanity}")  # prints current sanity
            hand.pop(use - 1)  # removes the card the player just used
            print(hand)  # shows remaining cards

    # when the player doesn't wanna play anymore
    elif action == "quit":
        print("Bye then. Here are the remaining cards in the stack.:")
        time.sleep(2)
        print(stack[number:])
        time.sleep(2)
        print("\nBest wishes.")
        time.sleep(2)
        quit()

def main():
    print("Welcome.")
    time.sleep(3)
    print("\nWARNING: This contains sensitive topics such as suicide and self-harm.\nFeel free to leave if you're uncomfortable.\n")
    time.sleep(3)
    while True:
        action = input("Have you played before? (y/n): ")
        if action.lower() == "no" or action.lower() == "n":
            text = """
        Hello then.
    
        start:
        - You have 5 cards
        - Stack has 65 cards
        - You have 10 sanity
        - Goal: Get to 100 sanity
        ways to end:
        - Finish the stack (bad)
        - Get to 0 or lower sanity (bad)
        - Get to 100 sanity (good)"""  # game instructions
            for line in text.splitlines():
                print(line)
                time.sleep(2)
            action = input("View card explanation? (y/n): ")
            if action.lower() == "y" or action.lower() == "yes":
                text = """
        cards:
        1. Kiyomi: Erologist
            - Gives 3 sanity
        2. Kiyomi: Fortune Teller
            - shows you the next 3 cards in the pile
        3. Kiyomi: Writer
            - 1:1 chance to get +3 or -3 sanity
        4. Mili: Lover
            - 1:1 chance to get +5 or -5 sanity
        5. Mili: Aichmophile
            - Gives a knife if your sanity is >=10
            - Takes 3 sanity if your sanity is <10
        6. Mili: Kura (short for sakura bc i wanna)
            - Gives 3 sanity
        7. Malika: Roll
            - You roll a dice and guess odd or even. Gives 3 sanity if correct, takes 3 sanity if not.
        8. Malika: Jackpot
            - Gives 3 sanity
        9. Malika: Tiandeng
            - Gives 5 sanity if your sanity is >=20.
            - Takes 5 sanity if your sanity is <20.
        10. Kzuhr: Lost Paradise
            - Takes 5 sanity
        11. Kzuhr: Sursurration
            - Gives 3 sanity
        12. Kaiin: Hide n' Seek
            - 1:2 chance to get -5 or +3 sanity
        13. Kaiin: Duty Calls
            - 1:1 chance of +3 or -5 sanity"""  # card explanation
                for line in text.splitlines():
                    print(line)
                    time.sleep(2)
            action = input("View card interaction explanation? (y/n): ")
            if action.lower() == "y" or action.lower() == "yes":
                text = """
        card interactions:
        "Kiyomi: Erologist" & "Mili: Lover"
        (when "Mili: Lover" is played)
            - 1:4 chance of -10 or +5 sanity
        Mili: Aichmophile & Kaiin: Duty Calls
        (when "Mili: Aichmophile" is played, acquiring the knife, before "Kaiin: Duty Calls")
            - Gives 5 sanity
            - Loss of the knife unless "Mili: Aichmophile" is played again
        "Mili: Kura" & "Kzuhr: Lost Paradise"
        (when "Mili: Kura" is played)
            - Gives 10 sanity
        (when "Kzuhr: Lost Paradise" is played)
            - Gives 5 sanity
        "Malika: Roll" & "Malika: Jackpot"
        (when "Malika: Roll" is played, and a loss is identified, before "Malika: Jackpot")
            - Number of losses in all "Malika: Roll" games are counted as pity. This number is added to the sanity gain in "Malika: Jackpot\""""  # card interactions
                for line in text.splitlines():
                    print(line)
                    time.sleep(2)
            break
        elif action.lower() == "y" or action.lower() == "yes":
            print("We shall start then,")
            time.sleep(2)
            break
        else:
            print("Please enter yes or no.")
            time.sleep(2)
    print("Starting game...")
    time.sleep(2)
    shuffling()  # calls shuffling to prepare the stack
    print("\nDrawing starting hand...")
    time.sleep(3)
    for i in range(5):
        drawing()  # gives the player their starting hand
    print(hand)

    # calls play() to start the card game
    while sanity > 0 and sanity < 100:
        play()

    # bad ending
    if sanity <= 0:
        print("""Death reached.

        See you on the other side! - Kiyo""")

    # good ending
    elif sanity >= 100:
        print("""Congrats! You live.

        I knew you could do it. - Kiyo""")
        action = input("\nView remaining cards? (y/n): ")
        if action.lower() == "y" or action.lower() == "yes":
            print(stack[number:])
            print(f"Remaining cards: {len(stack[number:])}") #shows the rest of the cards in the stack

main()
