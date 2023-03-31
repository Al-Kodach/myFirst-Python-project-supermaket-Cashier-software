def enterProducts(name, quantity):
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

    return buyingData
