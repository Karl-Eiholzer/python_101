import time
import math

'''Set parameters'''
run = 1

'''Define Functions'''
def yield_round(raw_yield):
    'Applies Rule G-33 yield rounding for an floating number input'
    n = float('%.4f'%(raw_yield))
    n = round(n,2)
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

def main():
    'Main Control Function'
    price_value_raw = raw_input('Enter the number you want formatted: ')
    price_value = float(price_value_raw)
    print('So you want ' + calc_type + ' and ' + str(price_value) + '?  OK')
    # Choose and call correct function
    if calc_type == 'Y':
        display_Y = yield_round(price_value)
        print('You have provided a yield')
        print('Correct display is: ' + str( display_Y ) )
    elif calc_type == 'D':
        display_DP = dollar_price_round(price_value)
        print('You have provided a dollar price')
        print('Correct display is: ' + str( display_DP ) )
    elif calc_type == 'A':
        display_AI = accrued_interest_round(price_value)
        print('You have provided accrued interest')
        print('Correct display is: ' + str( display_AI ) )

while run == 1:
    calc_type = raw_input('Enter type of price to input (A, D, Y, or Q): ')
    if calc_type == 'Q' or calc_type == 'q':
        print('You are bored already?')
        print('Good bye!!')
        run = 0
    elif calc_type == 'A' or calc_type == 'D' or calc_type == 'Y':
        main()
    else:
        print('Input not recognized. Try again')