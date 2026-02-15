import random
"""
Generate the UNO deck of 108 cards
No Parameters
Return the value(deck -> List)
"""

def build_deck():
    deck = []
    #example card: Red 7, Green 8, Blue Skip
    colours = ["Red", "Green", "Yellow","Blue"]
    values = [0,1,2,3,4,5,6,7,8,9, "Draw Two", "Skip", "Reverse"]
    wilds = ["wild", "Wild Draw Four"]
    for colour in colours:
        for value in values:
            card_val = f"{colour}, {value}"
            deck.append(card_val)
            if value != 0:
                deck.append(card_val)
    for i in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])            
    return deck  


"""
Shuffles a list of items passed into it
Parameters: deck -> list
Return values deck -> list
"""
def shuffle_deck(deck):
    for card_pos in range(len(deck)):
        rand_pos = random.randint(0, 107)
        deck[card_pos], deck[rand_pos] = deck[rand_pos], deck[card_pos]
    return deck

"""
Draw card function that draws a specific number of cards off the top of the deck
parameters: numCards -> interger
return cards drawn -> List
"""
def draw_cards(num_cards):
    cards_drawn = []
    for i in  range(num_cards):
        cards_drawn.append(uno_deck.pop(0))
    return cards_drawn
"""
prints formatted list of players hand
parameters: player -> integer, playerHand -> list
return: none
"""
def show_hand(player, player_hand):
    print(f"Player {player + 1}")
    print("Your Hand")
    print("--------------")
    for card in player_hand:
        print(card)
    print("")    

"""
Check whether a player is able to play a card, or not
parameters: discardCard->string, playerHand->list
return: Boolean
"""
def can_play(discard_card, player_hand):
    




uno_deck = build_deck()
uno_deck = shuffle_deck(uno_deck)
uno_deck = shuffle_deck(uno_deck)
discards = []
#print(uno_deck)

players = []
num_players = int(input("How many players? "))
while num_players < 2 or num_players > 4:
    num_players = int(input("Invalid. Please enter a number between 2-4. How many players? "))
for player in range(num_players):
    players.append(draw_cards(5))
    
player_turn = 0
player_direction = 1
playing = True
discards.append(uno_deck.pop(0))

while playing:
    show_hand(player_turn, players[player_turn])
    print(f"Card on top of discard pile: {discards[-1]}")

     







    