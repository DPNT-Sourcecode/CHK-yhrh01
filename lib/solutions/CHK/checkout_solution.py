from collections import defaultdict

PRICES = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10,
    'G': 20,
    'H': 10,
    'I': 35,
    'J': 60,
    'K': 80,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 30,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 90,
    'Y': 10,
    'Z': 50,
    
}

KNOWN_SKUS = PRICES.keys()

# Ordered list of offers. Offers with a higher count will appear first.
OFFERS = {
    'A': [
        {
            'count': 5,
            'value': 200
        },
        {
            'count': 3,
            'value': 130
        },
    ],
    'B': [
        {
            'count': 2,
            'value': 45
        }
    ],
    'H': [
        {
            'count': 10,
            'value': 80
        },
        {
            'count': 5,
            'value': 45
        }
    ],
    'K': [
        {
            'count': 2,
            'value': 150
        }
    ],
    '': [
        {
            'count': 0,
            'value': 0
        }
    ],
    '': [
        {
            'count': 0,
            'value': 0
        }
    ],
    '': [
        {
            'count': 0,
            'value': 0
        }
    ],
    '': [
        {
            'count': 0,
            'value': 0
        }
    ],
}

OFFER_SKUS = OFFERS.keys()

REDUCTION_OFFERS = {
    'E': {
        'count': 2,
        'reduction_sku': 'B',
        'reduction_count': -1
    },
    'F': {
        'count': 3,
        'reduction_sku': 'F',
        'reduction_count': -1
    }
}

REDUCTION_OFFERS_SKUS = REDUCTION_OFFERS.keys()

def _get_total_regular_price_for_basket_sku(sku: str, count: int):
    return PRICES[sku] * count

def _get_total_offer_price_and_remainder_for_basket_sku(sku: str, count: int) -> tuple[int, int]:
    running_sum = 0
    for offer in OFFERS[sku]:
        bundle_count = count // offer['count']
        remainder = count  % offer['count']
        if bundle_count == 0:
            continue
        else:
            running_sum += bundle_count * offer['value']
            count = remainder
    return running_sum, count

def _get_total_price_for_basket_sku(sku: str, count: int):
    if sku in OFFER_SKUS:
        offer_price_total, remainder = _get_total_offer_price_and_remainder_for_basket_sku(sku, count)
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
        _apply_reductions(basket_skus)
        total = 0
        for basket_sku, basket_sku_count in basket_skus.items():
            total += _get_total_price_for_basket_sku(basket_sku, basket_sku_count)
        return total        

