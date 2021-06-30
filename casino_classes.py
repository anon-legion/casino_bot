# Krzysztof requesting for comment regarding the direction I am taking before I proceed any further
cards_in_deck = [suit + str(val) for suit in 'CDHS' for val in [i for i in range(2, 10)] + [0] + ['J', 'Q', 'K', 'A']]


class Hand(object):
    def __init__(self):
        self._cards = []

    def __len__(self):
        return len(self.cards)

    def __iadd__(self, card):
        if type(card) == list:
            self.cards += card
        else:
            self.cards += [card]
        return self

    def __iter__(self):
        return iter(self._cards)

    def __repr__(self):
        return str(self.cards)

    @property
    def cards(self):
        return self._cards[:]
        # return self.getCards()

    @cards.setter
    def cards(self, cards):
        # create assertion for cards
        if type(cards) == list:
            self._cards = cards
        else:
            self._cards = [cards]

   # def getCards(self, isKeyOnly: bool = False, isImageOnly: bool = False) -> list:
   #      assert (type(isImageOnly) == bool and type(isKeyOnly) == bool) and not (isImageOnly and isKeyOnly)
   #      try:
   #          if isImageOnly:
   #              return [list(card.values())[0] for card in self._cards][:]
   #          elif isKeyOnly:
   #              return [list(card.keys())[0] for card in self._cards][:]
   #          else:
   #              return self._cards[:]
   #      except AssertionError:
   #          pass
   #          # invalid request operation

    def discard(self, card_choice=None):
        """
        discards a card from hand

        cardChoice: string (optional)
            assumes a string in cardsInDeck

        return: dictionary
            discarded card
        """
        assert len(self) > 0
        try:
            if card_choice is None:
                to_discard = self._cards.pop()
            else:
                index_of_card = self.cards.index(card_choice.upper())
                to_discard = self._cards.pop(index_of_card)
            return to_discard
        except (AssertionError, ValueError) as err:  # ValueError if .index() does not find cardChoice in self._cards
            print('Invalid move!')
            # invalid move operation

    def discard_hand(self):
        while len(self) > 0:
            self.discard()


class Player(object):
    def __init__(self, buyin, seatnum, is_dealer=False):
        self._balance = buyin
        self._seat = seatnum
        self._is_dealer = is_dealer

    def __iadd__(self, amount):
        self.balance = self.balance + amount
        return self

    def __isub__(self, amount):
        self.balance = self.balance - amount
        return self

    def __repr__(self):
        return str(self.balance)

    @property
    def balance(self):
        return self._balance

    @property
    def seat(self):
        return self._seat

    @property
    def is_dealer(self):
        return self._is_dealer

    @balance.setter
    def balance(self, amount):
        self._balance = amount

    @seat.setter
    def seat(self, num):
        self._seat = num

    @is_dealer.setter
    def is_dealer(self, button: bool):
        self._is_dealer = button

    def check(self):
        pass

    def bet(self, amount: int) -> int:
        assert type(amount) == int and (0 < amount <= self.balance)
        try:
            self.balance -= amount
            return amount
        except AssertionError:
            print('Invalid!')
            # invalid bet operation

    def call(self, to_call: int):
        assert type(to_call) == int
        try:
            if to_call > self.balance:
                self.all_in()
            else:
                self.bet(to_call)
        except AssertionError:
            print('Invalid')
            # invalid toCall

    def all_in(self):
        self.bet(self.balance)
