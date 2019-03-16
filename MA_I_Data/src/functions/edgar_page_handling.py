def edgar_MA_I_exists1(xml_url):
    'Return false if the xml page is not found'
    import urllib.request    
    print(xml_url)    
    return

def edgar_MA_I_exists(xml_url):
    'Return row of text describing the results'
    import requests
    import xml.etree.ElementTree as ET
    
    resp = requests.get(xml_url)
    return_code = resp.status_code

    if return_code == 200:
        root = ET.fromstring(resp.content)
        file_type = root[0][0].text  
    else:
        file_type = "Bad URL" 
    
    print(xml_url + "|" + str(return_code) + "|" + file_type)
    return


def get_url_list(location):
    import csv 
    out_list = list()
    with open(location, "r") as infile:
      reader = csv.reader(infile)
      next(reader, None)  # skip the headers
      for row in reader:
        # process each row
        out_list.append(row)     
    return(out_list)
    infile.close()

def get_url_list2(location):
    import csv 
    prefix = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK="
    suffix = "&type=&dateb=&owner=exclude&count=1000"
    out_list = list()
    with open(location, "r") as infile:
      reader = csv.reader(infile)
      next(reader, None)  # skip the headers
      for row in reader:
        # process each row
        created_URL = (prefix + str().join(row) + suffix)
        out_list.append(created_URL)     
    return(out_list)
    infile.close()

def get_868_number(cik_number):
    'return the 868 number associated with MA-I filings'
    import requests
    import re
    cik_url = ("https://www.sec.gov/cgi-bin/browse-edgar?CIK=" + cik_number + "&owner=exclude&action=getcompany")
    pattern = re.compile(r"868-\d{5}")
    
    resp = requests.get(cik_url)
    return_code = resp.status_code

    if return_code == 200:
        if "No matching CIK." in resp.text:
            file_type = "CIK Not Found"
        else:
            if pattern.search(resp.text) != None:
                file_type = "868 Number Found" 
            else:
                file_type = "868 Number Not Found" 
    else:
        file_type = "Bad URL" 
    
    print(cik_url + "|" + file_type + resp.text)
    return


def get_accession_numbers(cik_number):
    'return the 868 number associated with MA-I filings'
    import requests
    from html.parser import HTMLParser
    
    cik_url = ("https://www.sec.gov/cgi-bin/browse-edgar?CIK=" + cik_number + "&owner=exclude&action=getcompany")
    
    resp = requests.get(cik_url)
    return_code = resp.status_code
    edgar_page = HTMLParser.feed(resp)
           
    print(cik_url + "|" + edgar_page)
    return
