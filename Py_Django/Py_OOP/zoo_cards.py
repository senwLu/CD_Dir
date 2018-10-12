class Card:
    def __init__(self, value, type):
        self.value = value
        self.type = type

    def show(self):
        print('Value:', self.value, 'Type:', self.type)


class Deck:
    def __init__(self, name):
        self.deck = []
        self.name = name
        for i in ['clubs', 'diamonds', 'hearts', 'spades']:
            for j in range(1, 14):
                self.deck.append(Card(i, j))

    def show(self):
        for card in self.deck:
            card.show()


d1 = Deck("First deck")
d1.show()
