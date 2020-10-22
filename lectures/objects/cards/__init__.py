import check50
import uva.check50.py
import check50.internal
import sys
import os
import inspect

check50.internal.register.before_every(lambda : sys.path.append(os.getcwd()))
check50.internal.register.after_every(lambda : sys.path.pop())

suits = ['Hearts','Diamonds','Clubs','Spades']
values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
suits_set = set(suits)
values_set = set(values)


def all_list_in_set(lst, st):
    # check if all values in a list are in a set
    for string in lst:
        if not string in st:
            return False
        
    return True


def class_exists(module, cls):
    # check if the specified class exists
    if not hasattr(module, cls):
        raise check50.Failure(f"expected class '{cls}' to exist")


def attributes_present(obj, attributes):
    # check if each required attribute is present within the object
    for attribute in attributes:
        if not hasattr(obj, attribute):
            raise check50.Failure(f"expected class '{obj.__class__.__name__}' to have attribute '{attribute}'")


def class_method(cls, method):
    # check if method exists within class
    if not hasattr(cls, method) or not callable(getattr(cls, method)):
        raise check50.Failure(f"method '{method}()' does not exist within class '{cls.__name__}.")

def method_arguments(cls, method, required_args):
    # get args
    args = inspect.getfullargspec(getattr(cls, method)).args

    # check if the correct amount of arguments are present
    if len(required_args) != len(args):
        raise check50.Failure(f"method '{method}()' in class '{cls.__name__}' accepts {len(args)} argument(s). expected {len(required_args)}")

    # check if every required argument is present
    for arg in required_args:
        if not arg in args:
            raise check50.Failure(f"expected method '{method}()' in class '{cls.__name__}' to accept argument '{arg}'")


def deck_valid(deck):
     # check if 52 different and valid cards are present
    cards = set()

    # check amount of cards
    if len(deck._cards) != 52:
        raise check50.Failure(f"found invalid amount of cards {len(deck._cards)} in deck.")

    # check each card in the deck
    for card in deck._cards:
        # check for duplicate cards
        if card.suit + card.value in cards:
            raise check50.Failure(f"found the {card.value} of {card.suit} in deck at least twice.")
        cards.add(card.suit + card.value)

        # check if the card is valid
        if not card.value in values_set or not card.suit in suits_set:
            raise check50.Failure(f"found invalid card {card.value} of {card.suit} in deck.")


@check50.check()
def exists():
    """cardgame.py exists."""
    check50.exists("cardgame.py")


@check50.check(exists)
def compiles():
    """cardgame.py compiles."""
    uva.check50.py.compile("cardgame.py")
    module = uva.check50.py.run("cardgame.py").module


@check50.check(compiles)
def card_class_basic():
    """class 'Card' exists."""
    # check if the class exists
    module = uva.check50.py.run("cardgame.py").module
    class_exists(module, "Card")


@check50.check(card_class_basic)
def card_initializer():
    """class 'Card' can be initialized correctly."""
    module = uva.check50.py.run("cardgame.py").module

    # check if __init__ exists and accepts the correct args
    class_method(module.Card, "__init__")
    required_args = ["self", "suit", "value"]
    method_arguments(module.Card, "__init__", required_args)

    # loop through all possible cards
    for suit in suits:
        for value in values:
            card = module.Card(suit=suit, value=value)

            # check if the object has the required attributes
            attributes = ["suit", "value"]
            attributes_present(card, attributes)
            
            # check if the initializer worked
            if card.suit != suit:
                raise check50.Failure(f"class 'Card' was initialized with unexpected suit '{card.suit}'. expected '{suit}'")
            elif card.value != value:
                raise check50.Failure(f"class 'Card' was initialized with unexpected value '{card.value}'. expected '{value}'")


@check50.check(card_initializer)
def card_description():
    """method description() in class 'Card' returns the correct output."""
    module = uva.check50.py.run("cardgame.py").module

    # loop through all possible cards
    for suit in suits:
        for value in values:
            card = module.Card(suit=suit, value=value)

            # genererate description and check if the value is correct
            description = card.description().strip()
            if description != f"{value} of {suit}":
                raise check50.Failure(f"unexpected message '{description}' with suit '{suit}' and value '{value}'. expected '{value} of {suit}'")


@check50.check(card_description)
def deck_initializer():
    """class 'Deck' exists, has basic attributes and can be initialized correctly."""
    # check if the class exists
    module = uva.check50.py.run("cardgame.py").module
    class_exists(module, "Deck")

    # check if __init__ exists and accepts the correct args
    class_method(module.Deck, "__init__")
    required_args = ["self"]
    method_arguments(module.Deck, "__init__", required_args)

    # initialize a deck and check if it worked
    deck = module.Deck()

    # check if the object has the required attributes
    attributes = ["_suits", "_values"]
    attributes_present(deck, attributes)

    # check for correct initialization
    if not all_list_in_set(deck._suits, suits_set):
        raise check50.Failure("expected 'deck._suits' to contain all possible suits after initialization.")
    elif not all_list_in_set(deck._values, values_set):
        raise check50.Failure("expected 'deck._values' to contain all possible values after initialization.")


@check50.check(deck_initializer)
def instantiate_cards():
    """cards are instantiated in deck."""
    module = uva.check50.py.run("cardgame.py").module
    deck = module.Deck()

    # check if the class now has an attribute for storing cards
    attributes = ["_cards"]
    attributes_present(deck, attributes)

    # check if 52 different and valid cards are present
    deck_valid(deck)


@check50.check(instantiate_cards)
def shuffle():
    """deck changes and remains valid on shuffle()."""
    module = uva.check50.py.run("cardgame.py").module
    deck = module.Deck()

    # store original list of cards
    original_cards = [card.value + card.suit for card in deck._cards]

    # test if shuffle() exists and accept the correct arguments
    class_method(module.Deck, "shuffle")
    method_arguments(module.Deck, "shuffle", ["self"])

    # shuffle once
    deck.shuffle()

    # test if deck changed and is still valid
    new_cards = [card.value + card.suit for card in deck._cards]
    if all([original_cards[i] == new_cards[i] for i in range(len(new_cards))]):
        raise check50.Failure("deck didn't change when shuffled.")
    deck_valid(deck)


@check50.check(shuffle)
def deal():
    """deal() removes card and returns top card."""
    module = uva.check50.py.run("cardgame.py").module
    deck = module.Deck()
    deck.shuffle()

    # check if deal() exists and accepts the correct args
    class_method(module.Deck, "deal")
    method_arguments(module.Deck, "deal", ["self"])

    # vars to check against
    start_len = len(deck._cards)
    last_card = deck._cards[-1]

    # deal 52 cards
    for i in range(52):
        # update vars
        start_len = len(deck._cards)
        last_card = deck._cards[-1]

        # deal one card
        card = deck.deal()

        # check if deal decrements deck size by 1
        if len(deck._cards) != start_len - 1:
            raise check50.Failure(f"deal() changed amount of cards from {start_len} to {len(deck._cards)}. expected {start_len - 1}.")

        # check if we got the top card
        if card != last_card:
            raise check50.Failure(f"got unexpected card {card.value} of {card.suit} on deal() when top card was {last_card.value} of {last_card.suit}.")

        # check if the top card was removed, only run if there are any left
        if len(deck._cards) > 0:
            if deck._cards[-1] == last_card:
                raise check50.Failure(f"deal() removed a card other than the top card from the deck.")