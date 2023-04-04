#!/usr/bin/env python3
# we got cashier to input all products and store it in a dictionary
# each products value is the quantity
def enterProducts():
    buyingData = {}
    enterDetails = True

    # this loop will help cashier to continue entering product or disconnect from entering product
    while enterDetails:
        details = input(('Press A to add product or Q to quite:'))

        if details == 'A':
            product = input('Enter product:')
            quantity = int(input('Enter quantity:'))

            # we update the dictionary with the product name and quantity bought
            buyingData.update({product: quantity})

        elif details == 'Q':
            enterDetails = False

        else:
            print('Please select a correct option')

    return buyingData


# This function returns the subtotal of a single product as per it's price quantity.
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
    print(product + ':$' +
          str(priceData[product]) + 'x' + str(quantity) + '=' + str(subtotal))

    return subtotal


# This function decide if customer is qualified for a discount or not.
def getDiscount(billAmount, membership):
    discount = 0

    if billAmount >= 25:
        if membership == 'Gold':
            billAmount *= 0.80
            discount = 20

        elif membership == 'Silver':
            billAmount *= 0.90
            discount = 10

        elif membership == 'Bronze':
            billAmount *= 0.95
            discount = 5
        print(str(discount) + ' % off for ' + membership + ' ' +
              'membership on total amount: $' + str(billAmount))

    else:
        print('No discount on amount less than $25')
    return billAmount



def makeBill(buyingData, membership):
    billAmount = 0

    # we extract products name and quantity
    for key, value in buyingData.items():
        # we pass product name and quantity to getPrice() with returns a subtotal for each product
				# we add to billAmout for each subtotal
        billAmount += getPrice(key, value)

				# Finally we call getDiscount() and pass the total amount of products bought, this will return the discounted bill
        billAmount = getDiscount(billAmount, membership)

        print('The discounted amount is $:' + str(billAmount))


# The first line of excution will start from here
# Makes call to enterProduct() and store all product in buyingData varieble:
buyingData = enterProducts()

# This let cashier enters customers membership
membership = input('Enter customers membership:')

# we make a call to makeBill() passing products and membership as arguments
makeBill(buyingData, membership)
