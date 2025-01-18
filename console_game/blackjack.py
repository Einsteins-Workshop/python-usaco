# First, create an object that represents a deck of cards
class Deck:
    def __init__(self):
        # This represents all of the discarded cards
        self._discard = []
        # Create a list representing the deck of all cards not yet dealt out. This should be a set
        # of values representing a card. The values could be a number from 0 to 51, a string with
        # rank and suit, are a two element tuple with rank and suit. Make sure to save the deck to self.
        pass

    def deal_card(self):
        # This function should randomly deal a card from the not already dealt cards and remove it
        # from the deck.  It should return the dealt card.

        # Also, determine whether the deck should be reshuffled. This could be when all cards are dealt,
        # or when the cards get below some preset amount (like 10).
        pass

    def reshuffle(self):
        # Reshuffle the deck by adding the discard pile to the undealt cards
        pass

    def reset(self):
        # Set up the deck as it would be from the beginning, with all 52 cards
        pass


def card_name(value):
    # Given a card value, return the card name so that it is easy to understand
    pass

def blackjack_value(value):
    # Return the value of the card (1 for ace, 2-10 for other numbers, and 10 for Jack, Queen, and King
    pass

# Keep track of players and their current money

# Loop until players quit
    # Print out current players money totals
    # Ask if players want another hand
        # If players want to play, deal two cards to each player and to the house. Make sure that one
        # of the house cards is marked as hidden, and the other as shown.

        # Print out to all players their cards, and the revealed house card

        # Loop among all players
            # Ask (in a loop) if the player wants to hit (add another card)
                # If the player wants to hit, deal a card.
                    # If the players hand is over 21 (with aces evaluated as 1), declare that they bust
                # If the player does not want to hit, stop that player's loop and go to the next player

        # Reveal the house's hidden card

        # If any player has not bust, do the dealer's play
            # Deal (preferrably with a second of delay between cards) more cards to the dealer until
            # the dealer's total is 17 or more, with aces counted as 11 if it brings the total between 17-21
            # and 1 otherwise

        # Resolve all hands. Two card blackjacks automatically win, player busts automatically lose, if
        # the dealer busts, all non-busted players win, and otherwise anyone who has a higher total than
        # the dealer wins, lower totals lose, and tied totals draw. Update all player money totals.

# Other things to add:
# 1. Player blackjack hands (starting with an Ace and a 10, J, Q, or K) should result in an automatic win
# and 50% extra
# 2. Allow players to doube down when their starting total is 9, 10, or 11. They get exactly one dealt card,
# and win or lose double as normal
# 3. Allow players insurance-- if the dealer has an ace, all players may opt for insurance.  Anyone can pay
# half the bet for insurance. Then, check the dealer's hidden card. If it is 10, J, Q, or K, then anyone
# who has paid for insurance wins a full bet (basically are even for the hand), and anyone without a
# blackjack automatically loses. If the hidden card is not a 10, J, Q, or K, play continues as before and
# anyone who paid for insurance pays the half bet.
# 4. Splitting pairs-- if a player has a pair of the same denomination, they may split the cards into
# two separate hands with a full separate bet. Each hand is resolved in the normal way unless the player
# started with aces. Split aces only allow for a single card (for a total of two), and they do not get the
# blackjack bonus if they hit an ace-ten.

