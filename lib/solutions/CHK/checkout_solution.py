PRICES = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15
}

KNOWN_SKUS = PRICES.keys()

OFFERS = {
    'A': {
        'count': 3,
        'value': 130
    },
    'B': {
        'count': 2,
        'value': 45
    }
}

def get_price_for_sku():
    pass

def get_offer_price_for_sku():
    pass


class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        basket_skus = {}
        for sku in skus:
            if sku not in KNOWN_SKUS:
                return -1
            bas            
            pass



