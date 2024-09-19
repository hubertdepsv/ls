# 52 deck
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace
# Hearts, Diamonds, Clubs, Spades
# Dealer and Player
# Initial hand has 2 cards
# Player can see 1 of the dealer's cards + his own
# Values worth face value, >= Jack are worth 10 and Ace is 1 or 11
# Player always goes first
# Player chooses to hit (get another card) or stay
# Dealer always hits until the total is at least 17 then stays
# When both stay, we compare the values of both hands

# Pseudo code
# Initialise deck
# Draw 2 cards for the player
# Draw 2 cards for the dealer
# Turn 1
# Player turn
    #   Show one of the dealer's cards
    #   Show the player's cards
    #   Prompt the player for a choice
    #   If hit, draw a new card
    #   If stay, do nothing and go to the dealer
    #   Check if player is bust
# Dealer turn
    #   Compute hand value
    #   If < 17
    #   Hit draw a new card
    #   Else stay
# If the player also stayed show all cards
# Compute card values and announce the winner
# If the player didn't stay, start a new turn

import random

HEAD_VALUE = 10
BUST_VALUE = 21

def prompt(message):
    print(f"==> {message}")

def initialise_deck():
    return ['2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH',
             'QH', 'KH', 'AH',
            '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD',
              'QD', 'KD', 'AD',
            '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC',
              'QC', 'KC', 'AC',
            '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS',
              'QS', 'KS', 'AS']

def pick_a_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card

def initialise_hands(deck):
    player_hand = [pick_a_card(deck)]
    player_hand.append(pick_a_card(deck))
    dealer_hand = [pick_a_card(deck)]
    dealer_hand.append(pick_a_card(deck))
    return {'Player': player_hand, 'Dealer': dealer_hand}

# test cases
# test_deck = initialise_deck()
# test_card = pick_a_card(test_deck)
# print('Test card removed from deck?', test_card not in test_deck)
# print('Test deck has 1 less card?', len(test_deck) == 51)
# test_hands = initialise_hands(test_deck)
# print('Player hand:', test_hands['Player'])
# print('Dealer hand:', test_hands['Dealer'])
# print('Test deck has 5 less cards?', len(test_deck) == 47)

def compute_hand_value(hand):
    # takes a list as input
    result = 0
    aces = 0
    for card in hand:
        if card[0] in ['J', 'Q', 'K']:
            result += HEAD_VALUE
        elif card[0] == 'A':
            aces += 1
        else:
            result += int(card[0])

    if (result + 11) <= 21:
        result += 11
        aces -= 1

    if aces > 0: # might not be useful
        result += aces
    return result

# test cases
# print(compute_hand_value(['2S', '5S', 'JS']) == 17)
# print(compute_hand_value(['2S', '5S', 'JS', 'AS']) == 18)
# print(compute_hand_value(['2S', '5S', 'AS']) == 18)
# print(compute_hand_value(['2S', '5S', 'AS', 'AH']) == 19)

def is_bust(hand_values):
    for key, value in hand_values.items():
        if value > BUST_VALUE:
            return key
    return None

def find_winner():
    pass

# def player_hit_or_stay():
    # while True:
    #     prompt("Hit or stay?")
    #     answer = input().strip()
    #     if answer == 'Stay'
    # return 'Stay'

def dealer_hit_or_stay(hand):
    if compute_hand_value(hand) > 17:
        return 'Stay'
    return 'Hit'

def show_cards(hands):
    prompt('Here are the player\'s cards')
    print(f"{hands['Player']}")
    prompt(f"And one of the dealer's cards: {hands['Dealer'][0]}")

# game loop
deck = initialise_deck()
random.shuffle(deck)
hands = initialise_hands(deck)
hand_values = {
    'Player': compute_hand_value(hands['Player']),
    'Dealer': compute_hand_value(hands['Dealer']),
}

# start the loop and break if somebody gets bust
while True:
    show_cards(hands)

    prompt("Hit or Stay?")
    player_action = input().strip()
    if player_action == 'Hit':
        hands['Player'].append(pick_a_card(deck))
        hand_values['Player'] = compute_hand_value(hands['Player'])

    if is_bust(hand_values):
        prompt(f"{is_bust(hand_values)} is bust!")
        prompt(f"Hands are {hands}")
        prompt(f"Hand values: {hand_values}")
        break

    dealer_action = dealer_hit_or_stay(hands['Dealer'])
    if dealer_action == 'Hit':
        new_card = pick_a_card(deck)
        hands['Dealer'].append(new_card)
        hand_values['Dealer'] = compute_hand_value(hands['Dealer'])
        prompt('Dealer hits!')

    if is_bust(hand_values):
        prompt(f"{is_bust(hand_values)} is bust!")
        prompt(f"Hands are {hands}")
        prompt(f"Hand values: {hand_values}")
        break

    if (player_action == 'Stay') and (dealer_action == 'Stay'):
        prompt(f"Hands are {hands}")
        player_hand_value = compute_hand_value(hands['Player'])
        dealer_hand_value = compute_hand_value(hands['Dealer'])
        prompt(f"Hand values: {hand_values}")
        if player_hand_value >= dealer_hand_value:
            prompt("Player has won!")
        else:
            prompt("Computer has won!")
        break