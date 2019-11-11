import random


money = 100
def coin(bet, call):

    global money


    flip=random.randint(1,2)
    if call == "Heads" and flip == 1:
        money += bet
        print("The coin flip resulted in Heads. You won $" + str(bet) + ". You now have $" + str(money) + ".")
    elif call == "Tails" and flip == 2:
        money += bet
        print("The coin flip resulted in Tails. You won $" + str(bet) + ". You now have $" + str(money) + ".")
    elif call == "Heads" and flip == 2:
        money -=bet
        print("The coin flip resulted in Tails. You lost $ " + str(bet) + ". You now have $" + str(money) + ".")
    elif call == "Tails" and flip == 1:
        money -= bet
        print("The coin flip resulted in Heads. You lost $" + str(bet) + ". You now have $" + str(money) + ".")

def dice_game(bet, call):
    global money
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total=dice1+dice2
    if total % 2 == 1 and call == "Odd":
        money += bet
        print("The roll resulted in Odd. You won $" + str(bet) + ". You now have $" + str(money) + ".")
        print(total)
    elif total % 2 == 0 and call == "Even":
        money += bet
        print("The roll resulted in Even. You won $" + str(bet) + ". You now have $" + str(money) + ".")
        print(total)
    elif total % 2 == 1 and call == "Even":
        money -= bet
        print("The roll resulted in Odd. You lost $ " + str(bet) + ". You now have $" + str(money) + ".")
        print(total)
    elif total % 2 == 0 and call == "Odd":
        money -= bet
        print("The roll resulted in Even. You lost $ " + str(bet) + ". You now have $" + str(money) + ".")
        print(total)




def card_game(bet):
    global money
    card_one_value = random.randint(2, 14)
    card_two_value = random.randint(2, 14)
    card_one = card_one_value
    card_two = card_two_value
    if card_one_value == 11:
        card_one_ = "Jack"
    elif card_one_value == 12:
        card_one = "Queen"
    elif card_one_value == 13:
        card_one = "King"
    elif card_one_value == 14:
        card_one = "Ace"
    if card_two_value == 11:
        card_two = "Jack"
    elif card_two_value == 12:
        card_two = "Queen"
    elif card_two_value == 13:
        card_two = "King"
    elif card_two_value == 14:
        card_two = "Ace"
    if card_one_value > card_two_value:
        money+= bet
        print("Your card was: " + str(card_one) + ". My card was: " + str(card_two) + ". You won $" + str(bet) + ". You now have $" + str(money) + ".")
    elif card_one_value < card_two_value:
        money -= bet
        print("Your card was: " + str(card_one) + ". My card was: " + str(card_two) + ". You lost $ " + str(bet) + ". You now have $" + str(money) + ".")
    else:
        print("Your card was: " + str(card_one) + ". My card was: " + str(card_two) + ". It is a tie.")

coin(5, "Heads")
dice_game(5, "Odd")


