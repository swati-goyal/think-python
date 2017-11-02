from Card import *
from exercise_11 import invert_dict


class PokerHand(Hand):

    def suit_hist(self):
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def rank_hist(self):
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_pair(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False

    def has_two_pair(self):
        self.rank_hist()
        count = 0
        for val in self.ranks.values():
            if val >= 2:
                count += 1
        if count == 2:
            return True
        return False

    def has_three_of_a_kind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False

    def has_four_of_a_kind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val == 4:
                return True
        return False

    def has_full_house(self):
        if self.has_two_pair() and self.has_three_of_a_kind():
            return True
        return False

    def has_straight(self):
        self.rank_hist()
        t = sorted(list(self.ranks.keys()))
        r = get_combinations_of_hand_ranks(t)
        straights = get_straights()
        for x in r:
            if x in straights:
                return True
        return False

    def has_straight_flush(self):
        if self.has_flush() and self.has_straight():
            return True
        return False

    def classify(self):
        self.label = 'nothing'
        if self.has_straight_flush():
            self.label = 'straight-flush'
            return self.label
        elif self.has_four_of_a_kind():
            self.label = 'four-of-a-kind'
            return self.label
        elif self.has_full_house():
            self.label = 'full-house'
            return self.label
        elif self.has_flush():
            self.label = 'flush'
            return self.label
        elif self.has_straight():
            self.label = 'straight'
            return self.label
        elif self.has_three_of_a_kind():
            self.label = 'three-of-a-kind'
            return self.label
        elif self.has_two_pair():
            self.label = 'two-pair'
            return self.label
        elif self.has_pair():
            self.label = 'one-pair'
            return self.label
        return self.label


def get_straights():
    straights = []
    i = 1
    while i < 10:
        straights.append([i, i + 1, i + 2, i + 3, i + 4])
        i += 1
    straights.append([1, 13, 12, 11, 10])
    return straights


def get_combinations_of_hand_ranks(t):
    comb = []
    i = 1
    while i < (len(t) - 4):
        comb.append([t[i], t[i + 1], t[i + 2], t[i + 3], t[i + 4]])
        i += 1
    return comb


if __name__ == '__main__':
    some_list = {}
    # deal the cards and classify the hands
    for j in range(10000):
        # make a deck
        deck = Deck()
        deck.shuffle()
        for i in range(5):
            hand = PokerHand()
            deck.move_cards(hand, 7)
            hand.sort()
            some_list[hand.classify()] = some_list.get(hand.classify(), 0) + 1

    for key, value in some_list.items():
        some_list[key] = round(value/50000, 4)

    new_list = invert_dict(some_list)
    rankings = sorted(list(new_list.items()))
    for x in rankings:
        print(x)