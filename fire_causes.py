'''
Data Acquisition - Total Human and Lightning Caused Fires (2001-2018)
Cody Crofoot

This file pulls data from a government website and converts it into a csv document entitled big_fires.csv
Note This source contains 4 tables and creates 4 CSV
Note:  Western Great Basin Area combined with Eastern Great Basin Area in 2015.
       All previously reported statistics for Western Great Basin Area are included with Eastern Great Basin.
'''

import requests
import lxml.html as lh
import pandas as pd


url = 'https://www.nifc.gov/fireInfo/fireInfo_stats_lightng-human.html'
page = requests.get(url)

# Stores the contents of the website under doc
doc = lh.fromstring(page.content)

# print(page.text)

# Parse data that are stored between <tr>..</tr> of HTML
tr_elements = doc.xpath('//tr')
print(len(tr_elements))

'''

TABLE 1 -------------------------------------
NUMBER OF LIGHTNING FIRES (BY GEOGRAPHIC AREA)

'''

def get_lightning_fire_num():
    print("Number Lightning Fires (by Geographic Area")

    # Quick check to ensure all rows have the same width
    print([len(T) for T in tr_elements[:12]])

    # Stores the first element (header) and an empty list for each row
    lightning_fire_geo = []
    i = 0


    for t in tr_elements[1]:
        i += 1
        name = t.text_content()
        # print(i, name)
        lightning_fire_geo.append((name.replace(' ', '').replace('*', ''), []))


    for j in range(2, len(tr_elements)):
        # T is the j'th row
        T = tr_elements[j]

        # This refers back to our row width test and ensures each row should be the size of 3
        if len(T) != 13:
            break

        # Sets i as the index of the column
        i = 0
        for t in T.iterchildren():
            data = t.text_content()
            if i > 0:

                # Convert any numerical value to integers
                try:
                    data = int(data.title().replace("'", ""))
                except:
                    pass
            lightning_fire_geo[i][1].append(data)
            i += 1

    # Creates a dictionary with the data called wildfire
    num_lightning_fires = {title: column for (title, column) in lightning_fire_geo}
    # print(wildfire)

    # Converts all numbers to an int and any N/A to a null value
    for key in num_lightning_fires.keys():
        for i in range(len(num_lightning_fires[key])):
            if num_lightning_fires[key][i] == 'N/A':
                num_lightning_fires[key][i] = None
            elif type(num_lightning_fires[key][i]) != type(1):
                num_lightning_fires[key][i] = int(num_lightning_fires[key][i].replace(',', ''))

    # Creates a panda dataframe and csv from that
    df = pd.DataFrame(num_lightning_fires)
    print(df)

    df.to_csv('lightning_fire_num.csv', encoding='utf-8', index=False)


'''

TABLE 2 -------------------------------------
LIGHTNING ACRES (BY GEOGRAPHIC AREA)

'''

def get_lightning_fire_acres():
    print("Lightning Acres (by Geographic Area")

    # Quick check to ensure all rows have the same width
    print([len(T) for T in tr_elements[:12]])

    # Stores the first element (header) and an empty list for each row
    lightning_fire_acres = []
    i = 0


    for t in tr_elements[1+20]:
        i += 1
        name = t.text_content()
        # print(i, name)
        lightning_fire_acres.append((name.replace(' ','').replace('*', ''), []))


    for j in range(2+20, len(tr_elements)):
        # T is the j'th row
        T = tr_elements[j]

        # This refers back to our row width test and ensures each row should be the size of 3
        if len(T) != 13:
            break

        # Sets i as the index of the column
        i = 0
        for t in T.iterchildren():
            data = t.text_content()
            if i > 0:

                # Convert any numerical value to integers
                try:
                    data = int(data.title().replace("'", ""))
                except:
                    pass
            lightning_fire_acres[i][1].append(data)
            i += 1

    # Creates a dictionary with the data called wildfire
    size_lightning_fires = {title: column for (title, column) in lightning_fire_acres}
    print(size_lightning_fires)

    # Converts all numbers to an int and any N/A to a null value
    for key in size_lightning_fires.keys():
        for i in range(len(size_lightning_fires[key])):
            if size_lightning_fires[key][i] == 'N/A':
                size_lightning_fires[key][i] = None
            elif type(size_lightning_fires[key][i]) != type(1):
                size_lightning_fires[key][i] = int(size_lightning_fires[key][i].replace(',', ''))

    # Creates a panda dataframe and csv from that
    df = pd.DataFrame(size_lightning_fires)
    print(df)

    df.to_csv('lightning_fire_acres.csv', encoding='utf-8', index=False)


'''

Table 3 ------------------------------
Human Caused Fires (by Geographic Area)

'''

def get_human_fire_num():
    print("Human Caused Fires (by Geographic Area")

    # Quick check to ensure all rows have the same width
    print([len(T) for T in tr_elements[:12]])

    # Stores the first element (header) and an empty list for each row
    human_fires_num = []
    i = 0


    for t in tr_elements[1+20+20]:
        i += 1
        name = t.text_content()
        # print(i, name)
        human_fires_num.append((name.replace(' ',''), []))


    for j in range(2+20+20, len(tr_elements)):
        # T is the j'th row
        T = tr_elements[j]

        # This refers back to our row width test and ensures each row should be the size of 3
        if len(T) != 13:
            break

        # Sets i as the index of the column
        i = 0
        for t in T.iterchildren():
            data = t.text_content()
            if i > 0:

                # Convert any numerical value to integers
                try:
                    data = int(data.title().replace("'", ""))
                except:
                    pass
            human_fires_num[i][1].append(data)
            i += 1

    # Creates a dictionary with the data called wildfire
    num_human_fires = {title: column for (title, column) in human_fires_num}
    print(num_human_fires)

    # Converts all numbers to an int and any N/A to a null value
    for key in num_human_fires.keys():
        for i in range(len(num_human_fires[key])):
            if num_human_fires[key][i] == 'N/A':
                num_human_fires[key][i] = None
            elif type(num_human_fires[key][i]) != type(1):
                num_human_fires[key][i] = int(num_human_fires[key][i].replace(',', ''))

    # Creates a panda dataframe and csv from that
    df = pd.DataFrame(num_human_fires)
    print(df)

    df.to_csv('human_fire_num.csv', encoding='utf-8', index=False)




'''

Table 4 -------------------------------
Human Caused Acres (by Geographic Area)


'''

def get_human_fire_acres():
    print("Human Caused Acres (by Geographic Area")

    # Quick check to ensure all rows have the same width
    print([len(T) for T in tr_elements[:12]])

    # Stores the first element (header) and an empty list for each row
    human_fires_acres = []
    i = 0


    for t in tr_elements[1+20+20+20]:
        i += 1
        name = t.text_content()
        # print(i, name)
        human_fires_acres.append((name.replace(' ',''), []))


    for j in range(2+20+20+20, len(tr_elements)):
        # T is the j'th row
        T = tr_elements[j]

        # This refers back to our row width test and ensures each row should be the size of 3
        if len(T) != 13:
            break

        # Sets i as the index of the column
        i = 0
        for t in T.iterchildren():
            data = t.text_content()
            if i > 0:

                # Convert any numerical value to integers
                try:
                    data = int(data.title().replace("'", ""))
                except:
                    pass
            human_fires_acres[i][1].append(data)
            i += 1

    # Creates a dictionary with the data called wildfire
    size_human_fires = {title: column for (title, column) in human_fires_acres}
    print(size_human_fires)

    # Converts all numbers to an int and any N/A to a null value
    for key in size_human_fires.keys():
        for i in range(len(size_human_fires[key])):
            if size_human_fires[key][i] == 'N/A':
                size_human_fires[key][i] = None
            elif type(size_human_fires[key][i]) != type(1):
                size_human_fires[key][i] = int(size_human_fires[key][i].replace(',', ''))

    # Creates a panda dataframe and csv from that
    df = pd.DataFrame(size_human_fires)
    print(df)

    df.to_csv('human_fire_acres.csv', encoding='utf-8', index=False)



'''
Reference: https://towardsdatascience.com/web-scraping-html-tables-with-python-c9baba21059
'''