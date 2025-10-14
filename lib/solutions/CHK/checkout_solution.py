from collections import defaultdict

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

def _get_price_for_basket_sku(sku, count):
    pass

def _get_offer_price_for_basket_sku(sku, count):
    pass


class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus: str):
        basket_skus = defaultdict(int)
        for sku in skus:
            if sku not in KNOWN_SKUS:
                return -1
            basket_skus[sku] += 1
        for b




