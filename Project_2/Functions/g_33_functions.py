'''Define Functions'''
def yield_round(raw_yield):
    'Applies Rule G-33 yield rounding '
    from decimal import Decimal, ROUND_DOWN, ROUND_HALF_UP
    n1 = Decimal(raw_yield).quantize(Decimal('.0001'), rounding=ROUND_DOWN)
    n = Decimal(n1).quantize(Decimal('.001'), rounding=ROUND_HALF_UP)
    return n

def dollar_price_round(raw_DP):
    'Applies Rule G-33 dollar price rounding '
    from decimal import Decimal, ROUND_DOWN
    n = Decimal(raw_DP).quantize(Decimal('.001'), rounding=ROUND_DOWN)
    return n

def accrued_interest_round(raw_AI):
    'Applies Rule G-33 accrued interest rounding '
    from decimal import Decimal, ROUND_DOWN, ROUND_HALF_UP
    n1 = Decimal(raw_AI).quantize(Decimal('.001'), rounding=ROUND_DOWN)
    n = Decimal(n1).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
    return n