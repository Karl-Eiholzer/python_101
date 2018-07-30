def edgar_MA_I_exists1(xml_url):
    'Return false if the xml page is not found'
    import urllib.request
    print(xml_url)    
    return

def edgar_MA_I_exists(xml_url):
    'Return false if the xml page is not found'
    import urllib.request
    'REQUEST_TIMEOUT = 10'
    try:
        return_code = urllib.request.urlopen(xml_url)
        'return_code = urllib.request.urlopen(xml_url).code'
    except urllib.error.HTTPError as http_err:
        print(xml_url + "|" + "Error: %s" % http_err)
        return None
    return_code = urllib.request.urlopen(xml_url).code
    print(xml_url + "|" + str(return_code))
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

