'''Import necessary libraries'''

from pathlib import Path
from functions.edgar_page_handling import get_accession_numbers

'''set file location'''
url_list_file_location = Path("C:/Users/keiholzer/Documents/GitHub/python_101/MA_I_Data/data")
url_list_file_name = "url_list.csv"


'''Set loop parameters'''
run = 1
 

def create_master():
    'Will create the new master list of municipal advisors'
    print('')
    CIK_number = input('Enter CIK: ')
    print('')
    get_accession_numbers(CIK_number)
        
while run == 1:
    print('')
    print('Do you want to (1) create new master sheet, (2) test for exception cases and create list, or (q) quit?')
    repeat_greeting = input('What is your choice? (1, 2, or Q): ')
    if repeat_greeting == 'Q' or repeat_greeting == 'q':
        print('')
        print('You are bored already?')
        print('Good bye!!')
        print('')
        run = 0
    elif repeat_greeting.upper() == '1':
        print('You have chosen to create a new master sheet')
        print('This step will error out if you have not downloaded the correct spreadsheet from the SEC Web Site')
        create_master()
    else:
        print('Do you want to go or not? Try again')

