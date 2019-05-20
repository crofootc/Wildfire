'''
Data Acquisition - Supression Costs (1985-2018)
Cody Crofoot

This file pulls data from a government pdf and converts it into a csv document entitled big_fires.csv
Source: https://www.nifc.gov/fireInfo/fireInfo_documents/SuppCosts.pdf

'''

import PyPDF2
import pandas as pd
import urllib.request

def get_suppression_costs():
    # Extracts the pdf information as a string object
    pdfFileObj = open('SuppCosts.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # print(pdfReader.numPages)
    pageObj = pdfReader.getPage(0)
    pdfString = pageObj.extractText()
    # print(pdfString)
    pdfFileObj.close()

    # Test to make sure is a string
    # print(type(pdfString))

    # Changing the string object into a more manageable format
    data = pdfString.splitlines()
    title = data.pop(0)
    print(title, "\n")

    # Setting up the headers
    col_headers = []
    for i in range(6):
        col_headers.append(data.pop(0).replace(' ', ''))
    # print(col_headers)

    # Setting up the data for each column into their own list
    data_raw = data[0].split()
    # print(data_raw)
    for i in range(15):
        del data_raw[-1]
    # print("raw:", data_raw)
    years = []
    fires = []
    acres = []
    forestService = []
    doiAgencies = []
    total = []

    # Add data to each list
    for i in range(len(data_raw)):
        if i % 6 == 0:
            years.append(int((data_raw.pop(0)).title().replace("'", "")))
        if i % 6 == 1:
            fires.append(int((data_raw.pop(0)).replace(',', '').strip()))
        if i % 6 == 2:
            acres.append(float((data_raw.pop(0)).replace(',', '').replace('$', '').title().replace("'", "")))
        if i % 6 == 3:
            forestService.append(float((data_raw.pop(0)).replace(',', '').replace('$',' ').title().replace("'", "")))
        if i % 6 == 4:
            doiAgencies.append(float((data_raw.pop(0)).replace(',', '').replace('$', '').title().replace("'", "")))
        if i % 6 == 5:
            total.append(float((data_raw.pop(0)).replace(',', '').replace('$', '').title().replace("'", "")))

    # print(years, total)

    # Combining everything into a dictionary
    suppression = dict()
    suppression[col_headers[0]] = years
    suppression[col_headers[1]] = fires
    suppression[col_headers[2]] = acres
    suppression[col_headers[3]] = forestService
    suppression[col_headers[4]] = doiAgencies
    suppression[col_headers[5]] = total

    # print(suppression)

    # Creates a panda dataframe and csv from that
    df = pd.DataFrame(suppression)
    print(df)
    df.to_csv('suppression_costs.csv', encoding='utf-8', index=False)

'''
Reference: https://www.geeksforgeeks.org/working-with-pdf-files-in-python/
'''
