'''
Data Acquisition - Fires Greater than 100,000 acres (1997-2018)
Cody Crofoot

This file pulls data from a government website and converts it into a csv document entitled big_fires.csv
'''

import requests
import lxml.html as lh
import pandas as pd

def get_big_fires():
    url = 'https://www.nifc.gov/fireInfo/fireInfo_stats_lgFires.html'
    page = requests.get(url)

    # Stores the contents of the website under doc
    doc = lh.fromstring(page.content)



    # Parse data that are stored between <tr>..</tr> of HTML
    tr_elements = doc.xpath('//tr')


    # Quick check to ensure all rows have the same width
    print([len(T) for T in tr_elements[:12]])

    # Creates empty list
    col = []
    i = 0


    # Stores the first element (header) and an empty list for each row
    for t in tr_elements[0]:
        i += 1
        name = t.text_content()
        print(i, name)
        col.append((name.replace(' ',''), []))


    for j in range(1, len(tr_elements)):
        # T is the j'th row
        T = tr_elements[j]

        # This refers back to our row width test and ensures each row should be the size of 4
        if len(T) != 4:
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
            # col[i][1].append(data.title().replace(' ',''))

            i += 1

    # Creates a dictionary with the data called wildfire
    wildfire = {title: column for (title, column) in col}
    print(wildfire)

    # Converts year to integers
    for year in range(len(wildfire['Year'])):
        wildfire['Year'][year] = int(wildfire['Year'][year])

    # Converts Total Acres to a float
    for num in range(len(wildfire['TotalAcres'])):
        wildfire['TotalAcres'][num] = float(wildfire['TotalAcres'][num].replace(',', ''))


    # Creates a panda dataframe and csv from that
    df = pd.DataFrame(wildfire)
    print(df)

    df.to_csv('big_fires.csv', encoding='utf-8', index=False)


'''
Reference: https://towardsdatascience.com/web-scraping-html-tables-with-python-c9baba21059
'''


