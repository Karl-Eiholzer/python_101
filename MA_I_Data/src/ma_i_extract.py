'''Import necessary libraries'''


from Functions.extract_ma_i_fields import get_list_of_files

'''Set loop parameters'''
run = 1
  
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
    calc_type = raw_input('Want to go again? (Y or N): ')
    if calc_type == 'N' or calc_type == 'q':
        print('')
        print('You are bored already?')
        print('Good bye!!')
        print('')
        run = 0
    elif calc_type.upper() == 'Y':
        main()
    else:
        print('Input not recognized. Try again')