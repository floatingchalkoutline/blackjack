############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import random
import replit

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def player_hit():
    player_cards.append(cards[random.randint(0, 12)])

def dealer_hit():
    dealer_cards.append(cards[random.randint(0, 12)])

    

def current_standings():
    print(f"Your hand: {player_cards}")
    print(f"The dealer's first card is {dealer_cards[0]}")

playgame = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while playgame == "y":
    print(logo)
    players_turn = True
    dealers_turn = True
    player_cards = []
    dealer_cards = []
    player_hit()
    player_hit()
    dealer_hit()
    dealer_hit()
    player_total = sum(player_cards)
    dealer_total = sum(dealer_cards)
    if dealer_total == 21:
        print(f"Dealer has {dealer_cards}. Blackjack!\nYou lose!")
    elif player_total == 21:
        print(f"You have {player_cards}. Blackjack!\nYou win!")
    else:
        current_standings()
        #Player's turn
        while players_turn:
            hit = input("Would you like another card? Type 'y' or 'n': ")
            if hit == 'y':
                player_hit()
                if sum(player_cards) > 21 and 11 in player_cards:
                    ace_position = player_cards.index(11)
                    player_cards[ace_position] = 1
                    current_standings()
                elif sum(player_cards) > 21:
                    print(f"{player_cards}\n{sum(player_cards)}! You Bust!")
                    players_turn = False
                    dealers_turn = False
                    player_bust = True
                else:
                    current_standings()
            elif hit == 'n':
                if sum(player_cards) < 22:
                    player_bust = False
                players_turn = False
        #Dealer's turn
        while dealers_turn:
            while sum(dealer_cards) < 17:
                dealer_hit()
                if sum(dealer_cards) > 21 and 11 in dealer_cards:
                    ace_position = dealer_cards.index(11)
                    dealer_cards[ace_position] = 1
                    dealer_bust = False
                elif sum(dealer_cards) > 21:
                    print(f"Dealer's hand: {dealer_cards}\n{sum(dealer_cards)}! Dealer Bust! You win!")
                    players_turn = False
                    dealers_turn = False
                    dealer_bust = True
            if sum(dealer_cards) < 22:
                dealer_bust = False
            dealers_turn = False
        if not player_bust and not dealer_bust:
            if sum(player_cards) > sum(dealer_cards):
                print(f"Your hand: {player_cards}. Total: {sum(player_cards)}.\nDealer's hand: {dealer_cards}. Total: {sum(dealer_cards)}")
                print("You win!")
            elif sum(dealer_cards) > sum(player_cards):
                print(f"Your hand: {player_cards}. Total: {sum(player_cards)}.\nDealer's hand: {dealer_cards}. Total: {sum(dealer_cards)}")
                print("You lose!")
            elif sum(dealer_cards) == sum(player_cards):
                print(f"Your hand: {player_cards}. Total: {sum(player_cards)}.\nDealer's hand: {dealer_cards}. Total: {sum(dealer_cards)}")
                print("Draw!")

    playgame = input("Would you like to play again? Type 'y' or 'n': ")
    replit.clear()
