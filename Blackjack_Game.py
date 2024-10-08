import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
       # self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.deck.append(created_card)

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp+= '\n'+card.__str__()
        return "The deck has : "+deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

deck = Deck()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        # Track of aces whose value is 11
        if card.rank =='Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

hand = Hand()

class Chips:
    def __init__(self,total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

# Bet Amount
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Sorry, please provide an integer")
        else:
            if chips.bet > chips.total:
                print("Sorry, you do not have enough chips")
            else:
                break

def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    while True:
        x = input("Hit or Stand ? Enter h or s : ")
        if x[0].lower()=='h':
            hit(deck,hand)
        elif x[0].lower()=='s':
            print("Player Stands, Dealer's turn")
            playing = False
        else:
            print("Sorry invalid Input, Please enter h or s only")
            continue    # it is used , so that when we enter invalid input it should again ask user to provide input rather than breaking out of loop
        break

# To display cards

def show_some(player,dealer):
    # show only ONE of the dealer's card
    print("\n Dealer cards: ")
    print("First card is Hidden!")
    print(dealer.cards[1])

    # Show all cards of Player
    print("\n Player's cards: ")
    for card in player.cards:
        print(card)

def show_all(player,dealer):
    # Show all cards of Dealer
    print("\n Dealer's cards: ")
    for card in dealer.cards:
        print(card)
    print(f"Value of Dealer's card is : {dealer.value}")
    # Show all cards of Player
    print("\n Player's cards: ")
    for card in player.cards:
        print(card)
    print(f"Value of Player's card is : {player.value}")

# Functions to handle end of game scenarios

def player_busts(player,dealer,chips):
    print("Bust Player!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player Wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Bust Dealer!, Player wins")
    chips.lose_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer Wins!")
    chips.lose_bet()

def push(player,dealer,chips):
    print("Dealer and Player tie! PUSH")


    # MAIN GAME

while True:
    print("Welcome to BLACKJACK")

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand,dealer_hand)

    while playing:
        hit_or_stand(deck,player_hand)

        show_some(player_hand,dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

# If player hasn't busted, play Dealer's hand untill Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

        show_all(player_hand,dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif player_hand.value > dealer_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand,player_chips)

    print(f'\n Player Total Chips are at : {player_chips.total}')

    #Ask to play again
    new_game = input("Would you like to play another hand? y/n ")

    if new_game[0].lower()=='y':
        playing = True
        continue
    else:
        print("THANK YOU for Playing!")
        break
