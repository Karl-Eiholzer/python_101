'''Import necessary libraries'''

import csv
from pathlib import Path
from functions.edgar_page_handling import edgar_MA_I_exists, get_url_list

'''set file location'''
url_list_file_location = Path("C:\Projects\Python\MA_I_Data\data")
url_list_file_name = "url_list.csv"


'''Set loop parameters'''
run = 1
 

def main():
    'Main Control Function'
    print('')
    file_to_read = url_list_file_location / "url_list.csv"
    url_list = get_url_list(file_to_read)
    for row in url_list:
        character_row = str().join(row)
        edgar_MA_I_exists(character_row)
        
while run == 1:
    repeat_greeting = input('Go again? (Y or N): ')
    if repeat_greeting == 'N' or repeat_greeting == 'n':
        print('')
        print('You are bored already?')
        print('Good bye!!')
        print('')
        run = 0
    elif repeat_greeting.upper() == 'Y':
        main()
    else:
        print('Do you want to go or not? Try again')

