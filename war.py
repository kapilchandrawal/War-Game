from random import shuffle

suite = 'H D S C'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
class Deck:
    def __init__(self):
        self.deck_cards = [(s,r) for s in suite for r in ranks ]

    def shuffle(self):
        shuffle(self.deck_cards)

    def split_in_half(self):
        return (self.deck_cards[:26],self.deck_cards[26:])

class Hand:
    def __init__(self,cards):
        self.cards = cards

    def add_card(self,card):
        self.cards.extend(card)

    def remove_card(self):
        return self.cards.pop()

class Player:
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name,drawn_card))
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) > 3:
            return war_cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def more_cards(self):
        return len(self.hand.cards) != 0

d = Deck()
d.shuffle()
half1,half2 = d.split_in_half()
comp = Player("computer",Hand(half1))
name = input("What is your name player? ")
user = Player(name,Hand(half2))
total_rounds = 0
war_count = 0

while user.more_cards() and comp.more_cards():
    total_rounds += 1
    table_cards = []
    print(user.name+" count: "+str(len(user.hand.cards)))
    print(comp.name+" count: "+str(len(comp.hand.cards)))
    print('\n')

    c_card = comp.play_card()
    p_card = user.play_card()
    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        war_count +=1

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        c_card = comp.play_card()
        p_card = user.play_card()

        table_cards.append(c_card)
        table_cards.append(p_card)


        if ranks.index(c_card[1]) < ranks.index(p_card[1]):
            print(user.name+" has the higher card, adding to hand.")
            user.hand.add_card(table_cards)
        else:
            print(comp.name+" has the higher card, adding to hand.")
            comp.hand.add_card(table_cards)

    else:
        if ranks.index(c_card[1]) < ranks.index(p_card[1]):
            print(user.name+" has the higher card, adding to hand.")
            user.hand.add_card(table_cards)
        else:
            print(comp.name+" has the higher card, adding to hand.")
            comp.hand.add_card(table_cards)


