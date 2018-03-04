import time
import math
from Functions.g_33_functions import *

'''Set parameters'''
run = 1

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