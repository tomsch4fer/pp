"""Tom Schäfer, FPP WS23/24"""

""" TODO: tenäre Operatoren & List comprehensions um Code abzukürzen """

import random

class Card:
    """init-"""
    value = ''
    symbol = ''
    name = ''

def draw_card(discrad_pile):
    """ creates card with symbol, vaue & name-string & excludes doubled cards from game() """
    symbol = ['♣', '♦', '♥', '♠']
    value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass']
    card = Card()
    
    while True:
        card.symbol = random.choice(symbol)
        card.value = random.choice(value)
        card.name = f'{card.symbol}-{card.value}'
        
        """ no doubling - 52 unique cards """
        if card.name not in discrad_pile:
            discrad_pile.append(card.name)

            """ set comparison value based on index """
            card.value = value.index(card.value)
            card.symbol = symbol.index(card.symbol)
            """ hard return-- """
            return card

def game():
    """ compares 2 card values, sets score & allows abortion """
    score = 0
    discrad_pile = []
    active_card = draw_card(discrad_pile)

    print(f'Die aufgedeckte Karte ist {active_card.name}')
    
    for x in range(8):
        choice = input(f'{x+1}. Höher (h) oder Niedriger (n)?\n')
        
        if choice.lower() == 'a':
            print('Das Spiel wird abgebrochen.')
            break
        
        new_card = draw_card(discrad_pile)
        print(f'Die neue Karte ist {new_card.name}')
        
        """ logic too complex for single function-- """
        """ sprechende Variablennamen++ """   
        if choice.lower() == 'h':
            if active_card.value < new_card.value:
                print('Richtig! Die Karte ist höher.')
                score += 20
            # requirements modified: upon same value, symbol value is compared
            elif active_card.value == new_card.value:
                if active_card.symbol < new_card.symbol:
                    print('Richtig! Das Symbol ist höher.')
                    score += 20
                else:
                    print('Falsch! Das Symbol ist höher.')
                    score -= 15
            else:
                print('Falsch! Die Karte ist nicht höher.')
                score -= 15

        elif choice.lower() == 'n':
            if active_card.value > new_card.value:
                print('Richtig! Die Karte ist niedriger.')
                score += 20
            elif active_card.value == new_card.value:
                if active_card.symbol > new_card.symbol:
                    print('Richtig! Das Symbol ist niedriger.')
                    score += 20
                else:
                    print('Falsch! Das Symbol ist niedriger.')
                    score -= 15
            else:
                print('Falsch! Die Karte ist nicht niedriger.')
                score -= 15
        else:
            print('Ungültige Eingabe. Bitte wähle "h" für Höher, "n" für Niedriger oder "a" zum Abbrechen.')
            x -= 1

        active_card = new_card


    print(f'\nGG. Du hast {score} Punkte erreicht!\n')

if __name__ == "__main__":
    print("\nWillkommen zu 'Höher oder Niedriger'!\nDrücke \"a\" um abzubrechen.\n")
    game()