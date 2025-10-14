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

OFFER_SKUS = OFFERS.keys()

def _get_regular_price_for_basket_sku(sku: str, count: int):
    pass

def _get_offer_price_for_basket_sku(sku: str, count: int):
    pass

def _get_total_price_for_basket_sku(sku: str, count: int):
    if sku in OFFER_SKUS


class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus: str):
        basket_skus = defaultdict(int)
        for sku in skus:
            if sku not in KNOWN_SKUS:
                return -1
            basket_skus[sku] += 1
        total = 0
        for basket_sku, basket_sku_count in basket_skus.items():
            total += _get_total_price_for_basket_sku(basket_sku, basket_sku_count)
        