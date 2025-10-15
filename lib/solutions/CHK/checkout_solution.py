from collections import defaultdict

from .config import GROUP_OFFERS, PRICES, OFFERS, OFFER_SKUS, REDUCTION_OFFERS, KNOWN_SKUS

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

def _apply_group_offer(offer: dict, basket: dict) -> int:
    offer_skus = offer['skus']
    offer_skus_in_basket_count = sum(basket[sku] for sku in basket if sku in offer_skus)
    group_batches = offer_skus_in_basket_count // offer['count']
    reduction_count = offer_skus_in_basket_count - offer_skus_in_basket_count % offer['count']
    while reduction_count > 0:
        for offer_sku in offer_skus:
            if basket.get(offer_sku):
                basket[offer_sku] -= 1
                reduction_count -= 1
                if basket[offer_sku] == 0:
                    del basket[offer_sku]
    return group_batches * offer['value']
    pass


def get_total_price_for_basket_sku(sku: str, count: int):
    if sku in OFFER_SKUS:
        offer_price_total, remainder = _get_total_offer_price_and_remainder_for_basket_sku(sku, count)
        regular_price_total = _get_total_regular_price_for_basket_sku(sku, remainder)
        return offer_price_total + regular_price_total
    return _get_total_regular_price_for_basket_sku(sku, count)

def apply_reductions(basket_skus: dict[str, int]):
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

def apply_group_offers(basket: dict):
    group_offer_total = 0
    for offer in GROUP_OFFERS:
        _apply_group_offer(offer, basket)

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus: str):
        basket_skus = defaultdict(int)
        for sku in skus:
            if sku not in KNOWN_SKUS:
                return -1
            basket_skus[sku] += 1
        apply_reductions(basket_skus)
        group_offers_total = apply_group_offers(basket_skus)
        total = 0
        for basket_sku, basket_sku_count in basket_skus.items():
            total += get_total_price_for_basket_sku(basket_sku, basket_sku_count)
        return total        