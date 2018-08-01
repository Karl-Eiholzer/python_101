def edgar_MA_I_exists1(xml_url):
    'Return false if the xml page is not found'
    import urllib.request    
    print(xml_url)    
    return

def edgar_MA_I_exists(xml_url):
    'Return false if the xml page is not found'
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

