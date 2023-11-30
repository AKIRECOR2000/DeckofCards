import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
class Deck: 
    def __init__(self):
        self.ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.reset()
        
    def reset(self):
        self.deck = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
   
        
    def shuffle(self):
        random.shuffle(self.deck)
    
    
    def deal(self):
        if len(self.deck) == 0:
            return None
        return self.deck.pop()
        
   
    def count(self):
        return len(self.deck)
    
print("Card Dealer")
print("I've shuffled a deck of 52 cards.")
print()

deck = Deck()

deck.shuffle()

number_ofcards_todeal = int(input("How many cards would you like?: "))
print()
dealt_cards = []

for _ in range(number_ofcards_todeal):
    card = deck.deal()
    if card is not None:
        dealt_cards.append(f"{card.rank} of {card.suit}")
    else:
        print("There are no more cards in this deck.")
        print()
        
if dealt_cards:
    print("Dealt cards:")
    print()
    for card in dealt_cards:
        print(card)
        print()
    
count = deck.count()
print(f"Number of cards left in the deck: {count}")
print()

print("Good luck!")



 