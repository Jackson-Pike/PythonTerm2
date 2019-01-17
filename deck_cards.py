# Deck of Cards | Dec 2018
import random
# Lists
deck = []
player1_hand = []
player2_hand = []


def make_deck(deck):
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    VALUES = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    for e in SUITS:
        for i in VALUES:
            card = i + " of " + e
            deck.append(card)


def shuffle_deck(deck):
    for i in range(len(deck)):
        j = random.randrange(len(deck))
        temp = deck[i]
        deck[i] = deck[j]
        deck[j] = temp


def deal_card(deck, player1_hand, player2_hand):
    for i in range(5):
        card = deck.pop()
        player2_hand.append(card)
        card = deck.pop()
        player1_hand.append(card)
make_deck(deck)
shuffle_deck(deck)
deal_card(deck, player1_hand, player2_hand)
print(player1_hand)
print()
print(player2_hand)