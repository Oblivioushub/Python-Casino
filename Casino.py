import random

#list of cards in the order of there values. this is helpfull to both have every card and be able to compare their
# value to that of the list index.
cards = ['3D', '3C', '3H', '3S', '4D', '4C', '4H', '4S', '5D', '5C', '5H', '5S', '6D', '6C', '6H', '6S', '7D', '7C', '7H', '7S', '8D', '8C', '8H', '8S', '9D', '9C', '9H', '9S', '0D', '0C', '0H', '0S', 'JD', 'JC', 'JH', 'JS', 'QD', 'QC', 'QH', 'QS', 'KD', 'KC', 'KH', 'KS', 'AD', 'AC', 'AH', 'AS', '2D', '2C', '2H', '2S']
deck = ['3D', '3C', '3H', '3S', '4D', '4C', '4H', '4S', '5D', '5C', '5H', '5S', '6D', '6C', '6H', '6S', '7D', '7C', '7H', '7S', '8D', '8C', '8H', '8S', '9D', '9C', '9H', '9S', '0D', '0C', '0H', '0S', 'JD', 'JC', 'JH', 'JS', 'QD', 'QC', 'QH', 'QS', 'KD', 'KC', 'KH', 'KS', 'AD', 'AC', 'AH', 'AS', '2D', '2C', '2H', '2S']

#Create a shuffling function, where by when it is called to the deck is shuffled.
def shuffle():
    random.shuffle(deck)

#First Game: Higher or Lower
def higher_or_lower():
    #to begin we need a shuffled deck so we call to our previous function
    shuffle()

    counter = 0
    #current score of the player
    score = 0
    #create a response to refrence
    response = 1
    #while the user leaves a response
    while response:
        #show the user their current card ask them weather the bnext card will be higher or lower.
        response = input(f"The first card is {deck[counter]}. Do you belive the following card with g = greater or l = lower? (g/l) ")
        #if the card apears soon in the cards it has lower valueyy
        if cards.index(deck[counter]) < cards.index(deck[counter+1]):
            result = "g"
        else:
            result = "l"
        #increase counter
        counter+=1
        #tell user if they where right or wrong.
        if result == response.lower():
            print(f"Great job you got it correct! the card was {deck[counter]}.")
            score+=1
        else:
            print(f"Whoops! you got it wrong :(, the card was {deck[counter]}.")
    #game is over, tell the player there game score.
    print(f"Game over. Your score was {score}")

#Example of its use.
# higher_or_lower()

def slots():
    #greeting
    print("Welcome to the slot machine! Lets get started shall we? (to allow for speed you can simpily press enter/leave the input field empty to spin as much as you want)")
    #create possible items
    slot_items = ["♣️", "♦️", "♥️", "♠️"]
    #game is in play
    user_spin = True
    #start loop
    while user_spin:
        #slot machine output
        slot_line = [random.choice(slot_items), random.choice(slot_items), random.choice(slot_items)]
        print (slot_line) #showing it to user

        #if all the items in slot_line are equal
        if all(x == slot_line[0] for x in slot_line):
            user_input=input("You WON! do you want to spin again? (y/n) ") #The user won
        else:
            user_input=input("You Lost, do you want to spin again? (y/n) ") #The user lost :(
        if user_input.lower() == "y": #the user wants to play again
            user_spin = True
        elif user_input.lower() == "n": #the user does not want to play again.
            user_spin = False
        else:
            user_spin = True

def dice():
    print("Welcome to the Dice game! lets get started shall we? (to end game leave input field empty)")
    guess = True
    while guess:
        guess = input("What number do you think the dice will show? (1-12) ")
        dice = random.randrange(1, 13)
        if not(guess):
            print("Goodbye, You'll be back :D!")
        elif int(guess) in range(1, 13):
            print (f"The dice shows {dice}")
            if int(guess)==dice:
                print ("Great job, you guessed corectly!")
            else:
                print("You lost :(, you'll get them next time!")










#this function is for the blackjack game, helping to determine the numerical value of the cards.
def card_check(card, player, total):
    #if it is a picture card or a 10
    if card[0] == "0" or card[0] in ["J", "Q", "K"]:
        #the cards is worth 10
        return 10
    
    #if the card is a Ace and its the players
    elif card[0] == "A" and player:
        #if adding it dosen't make the player go bust
        if total+11 > 21:
            return 1
        #or dosent garantee a blackjack
        elif total+11 == 21:
            return 11
        #ask user what they want the ace to be worth
        else:
            print(f"Your current score is {total}.")
            ace_value = input("do you want the ace to be a 11 or a 1? (11/1) ")
            if ace_value == "1":
                return 1
            else:
                return 11
    #if the card is a ace and it is not the players
    elif card[0] == "A" and not player:
        #if +11 wont make the casino go bust
        if total+11 > 21:
            return 1
        #add the 11
        else:
            return 11
    #else use the number on the card to determine its value.
    else:
        return int(card[0])








#blackjack game
def blackjack():
    #grab the deck variable
    global deck

    #the dealer will shuffle the deck to begin.
    shuffle()

    #total variables defined
    user_total = 0
    casino_total = 0

    #user hand is drawn
    user_hand = [deck[0], deck[1]]
    #casino hand is drawn
    casino_hand = [deck[2], deck[3]]
    #cards are taken out of the deck.
    deck = deck[2:-4]

    #intro and dealers hand reveal
    print (f"Welcome to the digital blackjack tabble.")
    print (f"the dealers first card is {casino_hand[0]}")





    #User stuff \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
    for card in user_hand:
        user_total += card_check(card, True, user_total)

    player_bust = False

    #setting up players hand and getting their hits in.
    while True:
        print (f"Your hand is: {user_hand} which is equal to {user_total}")

        #if the user hits over 21
        if user_total > 21:
            player_bust = True
            print ("You got over 21! Dealer wins")
            break
        
        response = input("Do you want to hit? (y/n) ")
        if response.lower() == "y":
            user_hand.append(deck[0])
            deck.pop(0)
            user_total += card_check(user_hand[-1], True, user_total)

        else:
            break






    #casino Stuff \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

    #casino score is calculated
    for card in casino_hand:
        casino_total += card_check(card, False, casino_total)
    
    #tell the user the casinos hand and score
    print(f"The dealer's hand is {casino_hand} and there current score is {casino_total}")

    casino_bust = False

    while True:
        if casino_total < user_total and not player_bust:
            #casino will hit
            print("dealer hits.") #telling the user
            casino_hand.append(deck[0]) #adding the card
            deck.pop(0) #removing it from deck

            #adding that new card into their score
            casino_total += card_check(casino_hand[-1], False, casino_total)
            
            #tell the user the casinos full hand and current score.
            print(f"dealers's new hand is {casino_hand} and the score now is {casino_total}")

            #if the casino has just gone bust they have lost.
            if casino_total > 21:
                print(f"the dealer drew a {casino_hand[-1]}. That means they are bust!")
                casino_bust = True
                break

        else: #casino is sitting
            break



    if user_total > casino_total or casino_bust:
        #user wins
        print("YOU WIN!")
    elif user_total == casino_total:
        #its a tie
        print("Its a tie!")
    else:
        print("Oh no, you lost! Better luck next time")
    
    play_again = input("Do you want to play again? (y/n) ")

    if play_again != "n":
        blackjack()



#bot_ai a function designed to use the bots hand to determine what card they will play.
def bot_ai(hand, play_to_beat):
    if play_to_beat == None:
        return hand[0]
    else:
        for card in hand:
            if cards.index(card) > cards.index(play_to_beat):
                return card
        return None

def big_two():
    #grab the deck
    global deck

    #shuffle the cards
    shuffle()

    #it is the start of round
    play_to_beat = None
    
    #for when the game ends
    game_over = False

    #dealing the cards.
    hand1 = sorted(deck[:13], key=lambda x: cards.index(x))
    hand2 = sorted(deck[13:26], key=lambda x: cards.index(x))
    hand3 = sorted(deck[26:39], key=lambda x: cards.index(x))
    player_hand = sorted(deck[39:52], key=lambda x: cards.index(x))

    play_order = ["bot1", "bot2", "bot3", "player"]

    print("welcome to a digital game of Big Two!")
    print("Due to time dependinces this is only 1 card play big two.")
    print("Lets get started shall we?")
    print("----------------------------------")
    print (f"Your hand: {player_hand}")



    while True:
        if game_over:
            play_again = input("did you want to play again? (y/n) ").lower()
            if play_again == "y":
                big_two()
                break
            else:
                break
        #announce what round it is
        print(f"round comencing...")
        
        
        #determine who is starting the round
        if play_order[0] == "bot1":
            play_to_beat = bot_ai(hand1, play_to_beat)
            hand1.remove(play_to_beat)
            play_order.append(play_order.pop(play_order.index("bot1")))
            print(f"Bot1 plays {play_to_beat}")
            if len(hand1) == 0:
                print("Game over! bot 1 wins")
                game_over = True
                

        elif play_order[0] == "bot2":
            play_to_beat = bot_ai(hand2, play_to_beat)
            hand2.remove(play_to_beat)
            play_order.append(play_order.pop(play_order.index("bot2")))
            print(f"Bot2 plays {play_to_beat}")
            if len(hand2) == 0:
                print("Game over! bot 2 wins")
                game_over = True
                

        elif play_order[0] == "bot3":
            play_to_beat = bot_ai(hand3, play_to_beat)
            hand3.remove(play_to_beat)
            play_order.append(play_order.pop(play_order.index("bot3")))
            print(f"Bot3 plays {play_to_beat}")
            if len(hand1) == 0:
                print("Game over! bot 3 wins")
                game_over = True
                

        else: #player is starting the round
            print ("You are starting!")
            print(f"Your hand: {player_hand}")
            while True:
                play = input("what card do you want to play to start the round? (3D, KD, etc.) ").upper()
                if play:
                    if play in player_hand:
                        play_to_beat = play
                        print (f"Player plays {play_to_beat}")
                        player_hand.remove(play_to_beat)
                        
                        play_order.append(play_order.pop(play_order.index("player")))
                        break
                    else:
                        print ("that card is not in your hand!")
                        print ("Try again.")
                else:
                    print("pleas input a card.")
                    print ("Try again.")
            if len(hand1) == 0:
                print("Game over! bot 1 wins")
                game_over = True
        

        if game_over:
            play_again = input("did you want to play again? (y/n) ").lower()
            if play_again == "y":
                big_two()
                break
            else:
                break
        #announce what r

        bot1_pass = False
        bot2_pass = False
        bot3_pass = False
        player_pass = False

        while True:
            if play_order[0] == "bot1":
                if player_pass and bot2_pass and bot3_pass:
                    play_order = ["bot1", "bot2", "bot3", "player"]
                    break

                if bot1_pass:
                    play_order.append(play_order.pop(play_order.index("bot1")))
                else:
                    if bot_ai(hand1, play_to_beat):
                        play_to_beat = bot_ai(hand1, play_to_beat)
                        
                        print(f"Bot1 plays {play_to_beat}")
                        hand1.remove(play_to_beat)

                        if len(hand1) == 0:
                            print("Game over! bot 1 wins")
                            game_over = True
                            break
                    else:
                        bot1_pass = True
                        print ("Bot1 Passes.")
                    play_order.append(play_order.pop(play_order.index("bot1")))

            if play_order[0] == "bot2":
                if bot1_pass and player_pass and bot3_pass:
                    play_order = ["bot2", "bot3", "player", "bot1"]
                    break

                if bot2_pass:
                    play_order.append(play_order.pop(play_order.index("bot2")))
                else:
                    if bot_ai(hand2, play_to_beat):
                        play_to_beat = bot_ai(hand2, play_to_beat)
                        
                        print(f"Bot2 plays {play_to_beat}")
                        hand2.remove(play_to_beat)

                        if len(hand2) == 0:
                            print("Game over! bot 2 wins")
                            game_over = True
                    else:
                        bot2_pass = True
                        print ("Bot2 Passes.")
                    play_order.append(play_order.pop(play_order.index("bot2")))

            if play_order[0] == "bot3":
                if bot1_pass and bot2_pass and player_pass:
                    play_order = ["bot3", "player", "bot1", "bot2"]
                    break

                if bot3_pass:
                    play_order.append(play_order.pop(play_order.index("bot3")))
                else:
                    if bot_ai(hand3, play_to_beat):
                        play_to_beat = bot_ai(hand3, play_to_beat)
                        
                        print(f"Bot3 plays {play_to_beat}")
                        hand3.remove(play_to_beat)

                        if len(hand3) == 0:
                            print("Game over! bot 3 wins")
                            game_over = True
                            break
                    else:
                        bot3_pass = True
                        print ("Bot3 Passes.")
                    play_order.append(play_order.pop(play_order.index("bot3")))

            if play_order[0] == "player":
                if bot1_pass and bot2_pass and bot3_pass:
                    play_order = ["player", "bot1", "bot2", "bot3"]
                    break

                if player_pass:
                    play_order.append(play_order.pop(play_order.index("player")))
                else:
                    if cards.index(player_hand[-1]) > cards.index(play_to_beat):
                        print (f"Your turn, the play to beat is {play_to_beat}")
                        print(f"Your hand: {player_hand}")
                        print("leave the playing feild empty if you dont want to play")
                        while True:
                            play = input("what card do you want to play? (3D, KD, etc.) ").upper()
                            if play:
                                if play in player_hand:
                                    if cards.index(play) > cards.index(play_to_beat):
                                        play_to_beat = play
                                        print (f"Player plays {play_to_beat}")
                                        player_hand.remove(play_to_beat)
                                        break
                                else:
                                    print ("that card is not in your hand!")
                            else:
                                player_pass = True
                                print ("Player Passes.")
                                break
                        if len(player_hand) == 0:
                            print("Game over! Player wins")
                            game_over = True
                            break
                    else:
                        player_pass = True
                        print ("Player Passes.")
                    play_order.append(play_order.pop(play_order.index("player")))
        play_to_beat = None



#Game selection menu
print ("Welcome to the Casino! Hope you enjoy your stay")
while True:
    print ("What game would you like to play?")
    print ("(1) higher or lower")
    print ("(2) Slot Machine")
    print ("(3) Dice guesser")
    print ("(4) Blackjack")
    print ("(5) Big Two")
    game = input(">>> ")
    if game=="1":
        higher_or_lower()
    elif game=="2":
        slots()
    elif game=="3":
        dice()
    elif game=="4":
        blackjack()
    elif game=="5":
        big_two()
    else:
        print("Goodbye :D!")
        break