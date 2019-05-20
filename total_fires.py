'''
Data Acquisition - Total Wildland Fires and Acres (1926-2018)
Cody Crofoot

This file pulls data from a government website and converts it into a csv document entitled big_fires.csv
Note since prior to 1983, the sources cannot be confirmed so they are removed from the data
'''

import requests
import lxml.html as lh
import pandas as pd

def get_total_fires():
    url = 'https://www.nifc.gov/fireInfo/fireInfo_stats_totalFires.html'
    page = requests.get(url)

    # Stores the contents of the website under doc
    doc = lh.fromstring(page.content)

    # print(page.text)

    # Parse data that are stored between <tr>..</tr> of HTML
    tr_elements = doc.xpath('//tr')
    print(tr_elements)

    # Quick check to ensure all rows have the same width
    print([len(T) for T in tr_elements[:12]])

    # Creates empty list
    col = []
    i = 0

    # Stores the first element (header) and an empty list for each row
    for t in tr_elements[2]:
        i += 1
        name = t.text_content()
        print(i, name)
        col.append((name.replace(' ',''), []))


    for j in range(3, len(tr_elements)):
        # T is the j'th row
        T = tr_elements[j]

        # This refers back to our row width test and ensures each row should be the size of 3
        if len(T) != 3:
            break

        # Sets i as the index of the column
        i = 0
        for t in T.iterchildren():
            data = t.text_content()
            if i > 0:

                # Convert any numerical value to integers
                try:
                    data = int(data)
                except:
                    pass
            col[i][1].append(data.title().replace("'", ""))
            i += 1

    # Creates a dictionary with the data called wildfire
    wildfire = {title: column for (title, column) in col}
    print(wildfire)

    # Converts year to integers and removes data with years prior to 1983
    for year in range(len(wildfire['Year'])):
        wildfire['Year'][year] = int(wildfire['Year'][year])

    year = 0
    while year < len(wildfire['Year']):
        if wildfire['Year'][year] < 1983:
            del wildfire['Year'][year]
            del wildfire['Fires'][year]
            del wildfire['Acres'][year]
        elif wildfire['Year'][year] == 1926:
            del wildfire['Year'][year]
            del wildfire['Fires'][year]
            del wildfire['Acres'][year]
            break
        else:
            year += 1

    # Converts Fires to a float
    for num in range(len(wildfire['Fires'])):
        wildfire['Fires'][num] = float(wildfire['Fires'][num].replace(',', '').replace('*', ''))

    # Converts Acres to a float
    for num in range(len(wildfire['Acres'])):
        wildfire['Acres'][num] = float(wildfire['Acres'][num].replace(',', '').replace('*', ''))


    # Creates a panda dataframe and csv from that
    df = pd.DataFrame(wildfire)
    print(df)

    df.to_csv('total_fires.csv', encoding='utf-8', index=False)



'''
Reference: https://towardsdatascience.com/web-scraping-html-tables-with-python-c9baba21059
'''


