'''Import necessary libraries'''

import time
import math
from decimal import *
from Functions.g_33_functions import yield_round, dollar_price_round, accrued_interest_round

'''Set loop parameters'''
run = 1


def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput 
       break 
    
def main():
    'Main Control Function'
    print('')
    '''price_value_raw = raw_input('Enter the number you want formatted: ')'''
    Var = 1
    while Var > 0:
      try:
        price_value_raw = float(raw_input('Enter the number you want formatted: '))       
      except ValueError:
        print('')
        print("   ***   Not a valid number! Try again.   ***")
        print('')
        continue
      else:
        Var = Var -1     
    price_value = float(price_value_raw)
    print('')
    # Choose and call correct function
    if calc_type.upper() == 'Y':
        display_Y = yield_round(price_value)
        print('   You have provided a yield of ' + str(price_value) )
        print('')
        print('   Correct display is: ' + str( display_Y ) )
        print('')
    elif calc_type.upper() == 'D':
        display_DP = dollar_price_round(price_value)
        print('   You have provided a dollar price of ' + str(price_value) )
        print('')
        print('   Correct display is: ' + str( display_DP ) )
        print('')
    elif calc_type.upper() == 'A':
        display_AI = accrued_interest_round(price_value)
        print('   You have provided an accrued interest of ' + str(price_value) )
        print('')
        print('   Correct display is: ' + str( display_AI ) )
        print('')

while run == 1:
    calc_type = raw_input('Enter type of price to input (A, D, Y, or Q): ')
    if calc_type == 'Q' or calc_type == 'q':
        print('')
        print('You are bored already?')
        print('Good bye!!')
        print('')
        run = 0
    elif calc_type.upper() == 'A' or calc_type.upper() == 'D' or calc_type.upper() == 'Y':
        main()
    else:
        print('Input not recognized. Try again')