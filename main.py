#!/usr/bin/env python3

def enterProducts():
    buyingData = {}
    enterDetails = True

    while enterDetails:
        details = input(('Press A to add product or Q to quite:'))

        if details == 'A':
            product = input('Enter product:')
            quantity = int(input('Enter quantity:'))
            buyingData.update({product: quantity})

        elif details == 'Q':
            enterDetails = False

        else:
            print('Please select a correct option')

    return buyingData

def getPrice(product, quantity):
    priceData = {
        'Biscuit': 2,
        'Chicken': 6,
        'Egg': 1,
        'Fist': 4,
        'Coke': 2,
        'Bread': 2,
        'Apple': 3,
        'Onion': 3
    }

    subtotal = priceData[product] * quantity
    print(product + ':$' + str(priceData[product]) + 'x' + str(quantity) + '=' + str(subtotal))

    return subtotal
