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
    'P': [
        {
            'count': 5,
            'value': 200
        }
    ],
    'Q': [
        {
            'count': 3,
            'value': 80
        }
    ],
    'V': [
        {
            'count': 3,
            'value': 130
        },
        {
            'count': 2,
            'value': 90
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
    },
    'N': {
        'count': 3,
        'reduction_sku': 'M',
        'reduction_count': -1
    },
    'R': {
        'count': 3,
        'reduction_sku': 'Q',
        'reduction_count': -1
    },
    'U': {
        'count': 4,
        'reduction_sku': 'U',
        'reduction_count': -1
    },
}

REDUCTION_OFFERS_SKUS = REDUCTION_OFFERS.keys()

GROUP_OFFERS = {
    
}