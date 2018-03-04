'''Define Functions'''
def yield_round(raw_yield):
    'Applies Rule G-33 yield rounding for an floating number input'
    n = float('%.4f'%(raw_yield))
    n = round(n,3)
    return n

def dollar_price_round(raw_DP):
    'Applies Rule G-33 dollar price rounding for an floating number input'
    n = float('%.3f'%(raw_DP))
    return n

def accrued_interest_round(raw_AI):
    'Applies Rule G-33 accrued interest rounding for an floating number input'
    n = float('%.3f'%(raw_AI))
    n = round(n,2)
    return n