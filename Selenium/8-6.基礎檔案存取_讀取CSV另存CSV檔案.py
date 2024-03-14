import csv
infn = r'C:\Users\Roy\Documents\git\Python\Selenium\samples\csvReport.csv'
outfn = r'C:\Users\Roy\Documents\git\Python\Selenium\samples\csvOutport.csv'
with open(infn) as csvRfile:
    csvRfile = csv.reader(csvRfile)