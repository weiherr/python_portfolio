# Posted in replit on 23 April 2023 (https://replit.com/@weiherr/Blackjack-Project?v=1#main.py)
import random
from art import logo

def get_deck():
    suits = ["♦️", "♣️", "♥️", "♠️"]
    card_index = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    card = ""
    cards = []
    for value in card_index:
        for suit in suits:
            card = value + suit
            cards.append(card)
    return cards
    
def hit(party, deck):
    random_card = random.choice(deck)
    party.append(random_card)
    deck.remove(random_card)

def count_ace(party):
    count = 0
    for i in party:
        if i[0] == "A":
            count += 1
    return count
## testing of function check_ace
# test_player = ['3♦️', '4♣️']
# test_AI = ['3♦️', 'A♣️']
# print(check_ace(test_player))


def hand_value(party):
    value = 0
    card_values = {
        "A": 11,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "1": 10,
        "J": 10,
        "Q": 10,
        "K": 10
    }
    card_values_ace = {
        "A": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "1": 10,
        "J": 10,
        "Q": 10,
        "K": 10
    }
    for i in party:
        value += card_values[i[0]]
    if count_ace(party) == 2 and value > 21:
        value -= 20
    elif count_ace(party) == 1 and value > 21:
        value -= 10
    return value
## testing of function hand_value
# test_hand = ['K♠️', '7♦️']
# print(hand_value(test_hand))

def dealer_turn(party, deck):
    while hand_value(party) < 16:
        if len(party) <= 5:
            hit(party, deck)
    
def final_comparison(party_p, party_d):
    if hand_value(party_d) > 21 or hand_value(party_d) < hand_value(party_p):
        print(f"Your final hand: {party_p}, score: {hand_value(party_p)}\nComputer's final hand: {party_d}, score: {hand_value(party_d)}\nYou win!")
    elif hand_value(party_d) > hand_value(party_p):
        print(f"Your final hand: {party_p}, score: {hand_value(party_p)}\nComputer's final hand: {party_d}, score: {hand_value(party_d)}\nYou lose!")
    elif hand_value(party_d) == hand_value(party_p):
        print(f"Your final hand: {party_p}, score: {hand_value(party_p)}\nComputer's final hand: {party_d}, score: {hand_value(party_d)}\nIt's a draw!")
    else:
        print("Debugging required!!!")

def blackjack():
    print(logo)
    
    cards = get_deck()

    player = []
    dealer = []

    ## initial deal
    hit(player, cards)
    hit(dealer, cards)
    hit(player, cards)
    hit(dealer, cards)

    give_card = True

    if count_ace(player) >= 1 and hand_value(player) == 21:
        print(f"Your final hand :{player}, current score: {hand_value(player)}")
        print(f"Computer's final hand: {dealer}, final score: {hand_value(dealer)}")
        print("Win with a Blackjack 😎")
    elif count_ace(dealer) >= 1 and hand_value(dealer) == 21:
        print(f"Your final hand :{player}, current score: {hand_value(player)}")
        print(f"Computer's final hand: {dealer}, final score: {hand_value(dealer)}")
        print("Lose, opponent has Blackjack 😱")
    else:
        while give_card == True:
            print(f"Your cards :{player}, current score: {hand_value(player)}")
            print(f"Computer's first card: {dealer[0]}")

            if hand_value(player) > 21:
                give_card = False
                print(f"Your final hand: {player}, score: {hand_value(player)}\nComputer's final hand: {dealer}, score: {hand_value(dealer)}\nYou lose!")
            elif hand_value(player) < 21 and len(player) == 5:
                give_card = False
                print(f"Your final hand: {player}, score: {hand_value(player)}\nComputer's final hand: {dealer}, score: {hand_value(dealer)}\n五龙! You win!")
            elif hand_value(player) == 21 and len(player) == 5:
                give_card = False
                print(f"Your final hand: {player}, score: {hand_value(player)}\nComputer's final hand: {dealer}, score: {hand_value(dealer)}\n五龙廿一点! You win!")
            else:
                get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
                if get_another_card == "y":
                    hit(player, cards)
                elif get_another_card == "n":
                    give_card = False
                    dealer_turn(dealer, cards)

                    final_comparison(player, dealer)
 
start_or_not = input("Do you want to play a game of Blackjack? Type 'y' or 'n': " )
if start_or_not == 'y':
    next_game = True
    while next_game == True:
        blackjack()
        cont_play = input("Do you want to continue playing? Type 'y' or 'n': ")
        if cont_play == "n":
            next_game = False
        elif cont_play == "y":
            from replit import clear
            clear()
