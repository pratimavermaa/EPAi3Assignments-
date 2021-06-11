import random
from collections import Counter

value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']


def genrate_deck(value,suits):
  ''' This function takes suits and value list, combines them and returns the deck
    # Input :
        suits: list
        value: list
    # Functionality:
        Iterates over suits and value and combines each value.
    
    # Returns: 
        A list is returned containing the result of combination of value and suits.
    '''
  deck = []
  for number in value:
    for i in suits:
      card = i + str(number)
      deck.append(card)
  return deck

test_deck = genrate_deck(value,suits)
print(test_deck)

# Function generate deck of 52 cards Solely using map, lambda and zip function
def generate_deck_using_lambda_map_zip(value,suits):
  #using lambda zip and map fubction
  x = list(map(lambda cards: ''.join(cards), zip( suits*len(value),value*len(suits))))
  return x

test_list = generate_deck_using_lambda_map_zip(value,suits)
print(test_list)
