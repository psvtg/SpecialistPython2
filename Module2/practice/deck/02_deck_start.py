import random


values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
types = {'hearts': '\u2665',
         'diamonds': '\u2666',
         'clubs': '\u2663',
         'spades': '\u2660'}


class Card:
    def __init__(self, value, type):
        self.value = value
        self.type = type

    def to_str(self):
        return f"{self.value} {types[self.type]}"


class Deck:
    def __init__(self):
        self.cards = []

    def show(self):
        for card in self.cards:
            print(card.to_str())

    def draw(self, x):
        drawed = []
        for i in range(x):
            out = self.cards[i].pop()
            drawed.append(out.to_str())
        return drawed

    def shuffle(self):
        return random.shuffle(self.cards)


def main():
    mydeck = []
    for type in types:
        for value in values:
            card = Card(value, type)
            mydeck.append(card)

    deck = Deck()
    deck.cards = mydeck

    print(deck.show())
    deck.shuffle()
    print(deck.show())
    print('DRAW')
    print(deck.draw(5))



if __name__ == '__main__':
    main()
