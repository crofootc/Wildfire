'''
This file creates the tables for the database
Note this file treats each csv file as a separate database
'''

import pyodbc
import csv
import os

# Connecting to the database --
connection_string = f'Driver={{ODBC Driver 13 for SQL Server}};Server=stairway.usu.edu,1433;Database=codycrofoot;Uid={os.environ["SQLUserName"]};Pwd={os.environ["SQLPASSWORD"]}'
conn = pyodbc.connect(connection_string, autocommit=True)
print(conn)
curs = conn.cursor()


# Creating the BigFires Table
def create_BigFires():
    big_fires_col = list()
    with open('big_fires.csv') as f:
        reader = csv.reader(f)
        i = str(next(reader)).replace('[','').replace(']','').replace(',','').replace("'","")
        i = i.split()
        print(i, type(i))

        big_fires_col = i


    curs.execute(
        f'''
    
        CREATE TABLE BigFires(
        [generated_id] INT PRIMARY KEY CLUSTERED IDENTITY(1,1)
        ,{big_fires_col[0]} int
        ,{big_fires_col[1]} varchar(60)
        ,{big_fires_col[2]} varchar(2)
        ,{big_fires_col[3]} float
        ,
        )
    
    ''')

# Create the Total Fires Table
def create_TotalFires():
    total_fires_col = list()
    with open('total_fires.csv') as f:
        reader = csv.reader(f)
        i = str(next(reader)).replace('[','').replace(']','').replace(',','').replace("'","")
        i = i.split()
        print(i, type(i))

        total_fires_col = i
    # print(total_fires_col, type(total_fires_col))

    curs.execute(
        f'''
    
        CREATE TABLE TotalFires(
        [generated_id] INT PRIMARY KEY CLUSTERED IDENTITY(1,1)
        ,{total_fires_col[0]} int
        ,{total_fires_col[1]} float
        ,{total_fires_col[2]} float
        ,
        )
    
    ''')


##### Creates the human_fire_acres, human_fire_num, lightning_fire_acres, and lightning_fire_num tables

# Creates the human fire acres table
def create_HumanFireAcres():
    human_fire_acres_col = list()
    with open('human_fire_acres.csv') as f:
        reader = csv.reader(f)
        i = str(next(reader)).replace('[','').replace(']','').replace(',','').replace("'","")
        i = i.split()

        human_fire_acres_col = i

    # print(human_fire_acres_col)

    curs.execute(
        f'''
    
        CREATE TABLE HumanFireAcres(
        [generated_id] INT PRIMARY KEY CLUSTERED IDENTITY(1,1)
        ,{human_fire_acres_col[0]} int
        ,{human_fire_acres_col[1]} float
        ,{human_fire_acres_col[2]} float
        ,{human_fire_acres_col[3]} float
        ,{human_fire_acres_col[4]} float
        ,{human_fire_acres_col[5]} float
        ,{human_fire_acres_col[6]} float
        ,{human_fire_acres_col[7]} float
        ,{human_fire_acres_col[8]} float
        ,{human_fire_acres_col[9]} float
        ,{human_fire_acres_col[10]} float
        ,{human_fire_acres_col[11]} float
        ,{human_fire_acres_col[12]} float
        )
    ''')

# Creates the human fire number
def create_HumanFireNum():
    human_fire_num_col = list()
    with open('human_fire_num.csv') as f:
        reader = csv.reader(f)
        i = str(next(reader)).replace('[','').replace(']','').replace(',','').replace("'","")
        i = i.split()

        human_fire_num_col = i

    # print(human_fire_num_col)

    curs.execute(
        f'''
    
        CREATE TABLE HumanFireNum(
        [generated_id] INT PRIMARY KEY CLUSTERED IDENTITY(1,1)
        ,{human_fire_num_col[0]} int
        ,{human_fire_num_col[1]} float
        ,{human_fire_num_col[2]} float
        ,{human_fire_num_col[3]} float
        ,{human_fire_num_col[4]} float
        ,{human_fire_num_col[5]} float
        ,{human_fire_num_col[6]} float
        ,{human_fire_num_col[7]} float
        ,{human_fire_num_col[8]} float
        ,{human_fire_num_col[9]} float
        ,{human_fire_num_col[10]} float
        ,{human_fire_num_col[11]} float
        ,{human_fire_num_col[12]} float
        )
    ''')

# Creates the Lightning Fire Acres Table
def create_LightningFireAcres():
    lightning_fire_acres_col = list()
    with open('lightning_fire_acres.csv') as f:
        reader = csv.reader(f)
        i = str(next(reader)).replace('[','').replace(']','').replace(',','').replace("'","")
        i = i.split()

        lightning_fire_acres_col = i

    # print(lightning_fire_acres_col)

    curs.execute(
        f'''
    
        CREATE TABLE LightningFireAcres(
        [generated_id] INT PRIMARY KEY CLUSTERED IDENTITY(1,1)
        ,{lightning_fire_acres_col[0]} int
        ,{lightning_fire_acres_col[1]} float
        ,{lightning_fire_acres_col[2]} float
        ,{lightning_fire_acres_col[3]} float
        ,{lightning_fire_acres_col[4]} float
        ,{lightning_fire_acres_col[5]} float
        ,{lightning_fire_acres_col[6]} float
        ,{lightning_fire_acres_col[7]} float
        ,{lightning_fire_acres_col[8]} float
        ,{lightning_fire_acres_col[9]} float
        ,{lightning_fire_acres_col[10]} float
        ,{lightning_fire_acres_col[11]} float
        ,{lightning_fire_acres_col[12]} float
        )
    ''')

# Creates the Lightning Fire Num table
def create_LightningFireNum():
    lightning_fire_num_col = list()
    with open('lightning_fire_num.csv') as f:
        reader = csv.reader(f)
        i = str(next(reader)).replace('[','').replace(']','').replace(',','').replace("'","")
        i = i.split()

        lightning_fire_num_col = i

    # print(lightning_fire_num_col)

    curs.execute(
        f'''
    
        CREATE TABLE LightningFireNum(
        [generated_id] INT PRIMARY KEY CLUSTERED IDENTITY(1,1)
        ,{lightning_fire_num_col[0]} int
        ,{lightning_fire_num_col[1]} float
        ,{lightning_fire_num_col[2]} float
        ,{lightning_fire_num_col[3]} float
        ,{lightning_fire_num_col[4]} float
        ,{lightning_fire_num_col[5]} float
        ,{lightning_fire_num_col[6]} float
        ,{lightning_fire_num_col[7]} float
        ,{lightning_fire_num_col[8]} float
        ,{lightning_fire_num_col[9]} float
        ,{lightning_fire_num_col[10]} float
        ,{lightning_fire_num_col[11]} float
        ,{lightning_fire_num_col[12]} float
        )
    ''')




#### Creates the suppressionCost table
def create_SuppressionCosts():
    suppression_costs_col = list()
    with open('suppression_costs.csv') as f:
        reader = csv.reader(f)
        i = str(next(reader)).replace('[','').replace(']','').replace(',','').replace("'","")
        i = i.split()

        suppression_costs_col = i

    # print(suppression_costs_col)

    curs.execute(
        f'''
    
        CREATE TABLE SuppressionCosts(
        [generated_id] INT PRIMARY KEY CLUSTERED IDENTITY(1,1)
        ,{suppression_costs_col[0]} int
        ,{suppression_costs_col[1]} float
        ,{suppression_costs_col[2]} float
        ,{suppression_costs_col[3]} float
        ,{suppression_costs_col[4]} float
        ,{suppression_costs_col[5]} float
        )
    ''')
