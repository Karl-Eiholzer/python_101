'''Import necessary libraries'''

from pathlib import Path
import requests
from functions.edgar_page_handling import get_url_list2
from bs4 import BeautifulSoup

'''set file location'''
url_list_file_location = Path("C:/Users/keiholzer/Documents/GitHub/python_101/MA_I_Data/data")
url_list_file_name = "CIK_list_test.csv"


'''Set loop parameters'''
run = 1
 


def main():
    'Main Control Function'
    'return the Accession Filings associated with a CIK number'

    "Load List of CIK Numbers"
    file_to_read = url_list_file_location / url_list_file_name
    CIK_list = get_url_list2(file_to_read)
    
    for row in CIK_list:
        character_row = str().join(row)
        resp = requests.get(character_row)
        return_code = resp.status_code
        soup = BeautifulSoup(resp.text, 'html.parser')
        if soup.title.text == "EDGAR Search Results":
            print(soup.title.text)
        
# =============================================================================
#         if return_code == 200:
#             scrape_accession_numbers(CIK_url)
# =============================================================================
       
 # =============================================================================
#         print(CIK_url + "|" + return_code)
#         resp = requests.get(cik_url)
#         return_code = resp.status_code
#         edgar_page = HTMLParser.feed(resp)
# =============================================================================
   
       
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

