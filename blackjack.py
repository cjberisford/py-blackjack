# blackjack.py

from cards import Card, Deck

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

playing_cards = [Card(rank, suit) for suit in suits for rank in ranks]
main_deck = Deck('Main', playing_cards)
discard_pile = Deck('Discard', [])
player_hand = Deck('Player Hand', [])
dealer = Deck('Dealer', [])

def hand_value(deck):
    total = sum([card.value for card in deck.cards])
    
    # adjust values of aces
    if total > 21:
        # Update aces in hand to be 1
        [card.setValue(1) for card in deck.cards if card.rank == 'Ace']
        total = sum([card.value for card in deck.cards])

    return total

def deal_cards(from_deck, to_deck, n_cards):
    for _ in range(n_cards):
        card = from_deck.draw_card()
        to_deck.add_card_to_deck(card)

def display_hand(deck):
    print(f'{deck.name} value is {hand_value(deck)} {[str(card) for card in deck.cards]}')

# Deal initial cards
deal_cards(main_deck, player_hand, 2)

# Main game loop
print("Welcome to BlackJack")
while True:
    display_hand(player_hand)
    if (hand_value(player_hand) > 21):
        print('Bust!! You lose')
        break
    response = input(f'Stick or twist? ').lower()
    if response == 'twist': 
        deal_cards(main_deck, player_hand, 1)
    elif response == 'stick':
        print('Locked in, dealer plays...')
        break
    else:
        print('Invalid input')

# Dealer's turn
while hand_value(dealer) < 17:
    deal_cards(main_deck, dealer, 1)

# Display final hands
display_hand(player_hand)
display_hand(dealer)

# Determine the winner
if (hand_value(player_hand) > 21):
    print("You lose.")
elif (hand_value(dealer) > 21):
    print("You win!")
elif hand_value(player_hand) > hand_value(dealer):
    print("You win!")
elif hand_value(player_hand) < hand_value(dealer):
    print("You lose.")
else:
    print("It's a tie!")