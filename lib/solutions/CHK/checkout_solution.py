from collections import defaultdict

PRICES = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15
}

KNOWN_SKUS = PRICES.keys()

OFFERS = {
    'A': [{
        'count': 3,
        'value': 130
    }],
    'B': {
        'count': 2,
        'value': 45
    }
}

OFFER_SKUS = OFFERS.keys()

REDUCTION_OFFERS = {
    'E': {
        'count': 2,
        'reduction_sku': 'B',
        'reduction_count': -1
    }
}

REDUCTION_OFFERS_SKUS = REDUCTION_OFFERS.keys()

def _get_total_regular_price_for_basket_sku(sku: str, count: int):
    return PRICES[sku] * count

def _get_total_offer_price_for_basket_sku(sku: str, count: int):
    bundle_count = count // OFFERS[sku]['count']
    return bundle_count * OFFERS[sku]['value']

def _get_total_price_for_basket_sku(sku: str, count: int):
    if sku in OFFER_SKUS:
        remainder = count % OFFERS[sku]['count']
        offer_price_total = _get_total_offer_price_for_basket_sku(sku, count - remainder)
        regular_price_total = _get_total_regular_price_for_basket_sku(sku, remainder)
        return offer_price_total + regular_price_total
    return _get_total_regular_price_for_basket_sku(sku, count)

def _apply_reductions(basket_skus: dict[str, int]):
    to_reduce = {}
    for sku, count in basket_skus.items():
        if sku in REDUCTION_OFFERS:
            bundles = count // REDUCTION_OFFERS[sku]['count']
            sku_to_reduce = REDUCTION_OFFERS[sku]['reduction_sku']
            to_reduce[sku_to_reduce] = bundles * REDUCTION_OFFERS[sku]['reduction_count']
    for sku, reduction_count in to_reduce.items():
        basket_skus[sku] += reduction_count
        if basket_skus[sku] <= 0:
            del basket_skus[sku]

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
        return total        


