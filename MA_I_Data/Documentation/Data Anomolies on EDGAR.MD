## Data Anomolies on EDGAR
The problems identified below may require special handling by the code.


**1. Certain filings do not have a mismatch between the CIK number of the Filer page URL and the CIK of the Acession Number**

  Example 1: 0000786671 and 0000734903


  https://www.sec.gov/Archives/edgar/data/734903/000078667114000039/primary_doc.xml



  Example 2: 0000312603 and 0001615126


  https://www.sec.gov/Archives/edgar/data/1615126/000031260314000039/primary_doc.xml



  Example 3: 0001631061 and 0001615947 and 0000950123 and 0001564590


  https://www.sec.gov/Archives/edgar/data/1631061/000095012317008486/primary_doc.xml

  https://www.sec.gov/Archives/edgar/data/1615947/000095012314009895/primary_doc.xml

  https://www.sec.gov/Archives/edgar/data/1631061/000156459015005207/primary_doc.xml

  

  Example 4: 0001282186 and 0001140361  <== not a single filing for this firm has a match

  https://www.sec.gov/Archives/edgar/data/1282186/000114036114039531/primary_doc.xml


  Example 5: 0001603788 and 0000947871

  https://www.sec.gov/Archives/edgar/data/1603788/000094787117000875/primary_doc.xml



  


**2. Certain companies have Accession Number filing systems that do not follow the standard. You cannot assume the first filing for the year was anywhere near the number 1.

  Example 1: 0001663526 has the following number assigned to the first filings of the year:
   2016: 012963
   2017: 003002

  https://www.sec.gov/cgi-bin/browse-edgar?CIK=0001663526&owner=exclude&action=getcompany


  Example 2: 0001631061 / 0001615947 / 0001623553 has the following number assigned to the first filings of the year:
   2014 for 0001615947: 009895
   2014 for 0001623553: 010786
   2015 for 0001631061: 000637
   2016 for 0001623553: 025063
   2017 for 0001631061: 000675

  Pattern returns to normal for 0001615947 in 2015 (starts with 000002) - **but also has CIK number change - see example 3 under problem 1 above** 

  https://www.sec.gov/cgi-bin/browse-edgar?CIK=0001615947&owner=exclude&action=getcompany


  Example 3: 0001282186 (0001140361?) has the following number assigned to the first filings of the year:
   2014: 039526
   2015: 017240 
   2016: 059686

  None of the accession numbers for this firm use the  CIK shown on the filer page - see example 4 above

  https://www.sec.gov/cgi-bin/browse-edgar?CIK=0001615947&owner=exclude&action=getcompany


  Example 4: 0000769993 has the following number assigned to the first filings of the year:
    2016: 001496


  Example 5: 0001603788 / 0000947871 has the following number assigned to the first filings of the year:
    2016: 000875
