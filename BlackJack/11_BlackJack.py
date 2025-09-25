import Black_jack_art
import random

print(Black_jack_art.logo)

user_cards = []
computer_cards = []

def deal_card():
    """ Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

for _ in range(2):
    '''Assign new initial cards to players'''
    user_cards.append(deal_card())
    computer_cards.append(deal_card())