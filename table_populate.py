import pyodbc
import csv
import os

# Connecting to the database
connection_string = f'Driver={{ODBC Driver 13 for SQL Server}};Server=stairway.usu.edu,1433;Database=codycrofoot;Uid={os.environ["SQLUserName"]};Pwd={os.environ["SQLPASSWORD"]}'
conn = pyodbc.connect(connection_string, autocommit=True)
print(conn)
curs = conn.cursor()

### BigFires
def populate_big_fires():
    with open ('big_fires.csv', 'r') as f:
        reader = csv.reader(f, )
        columns = next(reader)
        print("\n\n\n-----------Populating BigFires-------------\n")

        for data in reader:
            query = 'insert into BigFires({0})'

            query = query.format(','.join(columns), ','.join('?' * (len(columns) - 1)))

            col = str(data[0])
            for i in range(len(data)-1):
                if type(data[i+1]) == type('string'):
                    col = col + ",'" + str(data[i + 1]) + "'"
                else:
                    col = col + "," + str(data[i+1])
            query = query + f' values ({col});'
            print(query)

            curs.execute(query)
        curs.commit()



### TotalFires
def populate_total_fires():
    with open ('total_fires.csv', 'r') as f:
        reader = csv.reader(f, )
        columns = next(reader)
        print("\n\n\n-----------Populating TotalFires-------------\n")

        for data in reader:
            query = 'insert into TotalFires({0})'

            query = query.format(','.join(columns), ','.join('?' * (len(columns) - 1)))

            col = str(data[0])
            for i in range(len(data)-1):
                if type(data[i+1]) == type('string'):
                    col = col + ",'" + str(data[i + 1]) + "'"
                else:
                    col = col + "," + str(data[i+1])
            query = query + f' values ({col});'
            print(query)

            curs.execute(query)
        curs.commit()


### HumanFireAcres
def populate_human_fire_acres():
    with open ('human_fire_acres.csv', 'r') as f:
        reader = csv.reader(f, )
        columns = next(reader)
        print("\n\n\n-----------Populating HumanFireAcres-------------\n")


        for data in reader:
            query = 'insert into HumanFireAcres({0})'

            query = query.format(','.join(columns), ','.join('?' * (len(columns) - 1)))

            col = str(data[0])
            for i in range(len(data)-1):
                if type(data[i+1]) == type('string'):
                    col = col + ",'" + str(data[i + 1]) + "'"
                else:
                    col = col + "," + str(data[i+1])
            query = query + f' values ({col});'
            print(query)

            curs.execute(query)
        curs.commit()


### HumanFireNum
def populate_human_fire_num():
    with open ('human_fire_num.csv', 'r') as f:
        reader = csv.reader(f, )
        columns = next(reader)
        print("\n\n\n-----------Populating HumanFireNum-------------\n")


        for data in reader:
            query = 'insert into HumanFireNum({0})'

            query = query.format(','.join(columns), ','.join('?' * (len(columns) - 1)))

            col = str(data[0])
            for i in range(len(data)-1):
                if type(data[i+1]) == type('string'):
                    col = col + ",'" + str(data[i + 1]) + "'"
                else:
                    col = col + "," + str(data[i+1])
            query = query + f' values ({col});'
            print(query)

            curs.execute(query)
        curs.commit()


### LightningFireAcres
def populate_lightning_fire_acres():
    with open ('lightning_fire_acres.csv', 'r') as f:
        reader = csv.reader(f, )
        columns = next(reader)
        print("\n\n\n-----------Populating LightningFireAcres-------------\n")


        for data in reader:
            query = 'insert into LightningFireAcres({0})'

            query = query.format(','.join(columns), ','.join('?' * (len(columns) - 1)))

            col = str(data[0])
            for i in range(len(data)-1):
                if type(data[i+1]) == type('string'):
                    col = col + ",'" + str(data[i + 1]) + "'"
                else:
                    col = col + "," + str(data[i+1])
            query = query + f' values ({col});'
            print(query)

            curs.execute(query)
        curs.commit()


### LightningFireNum
def populate_lightning_fire_num():
    with open ('lightning_fire_num.csv', 'r') as f:
        reader = csv.reader(f, )
        columns = next(reader)
        print("\n\n\n-----------Populating LightningFireNum-------------\n")


        for data in reader:
            query = 'insert into LightningFireNum({0})'

            query = query.format(','.join(columns), ','.join('?' * (len(columns) - 1)))

            col = str(data[0])
            for i in range(len(data)-1):
                if type(data[i+1]) == type('string'):
                    col = col + ",'" + str(data[i + 1]) + "'"
                else:
                    col = col + "," + str(data[i+1])
            query = query + f' values ({col});'
            print(query)

            curs.execute(query)
        curs.commit()


### SuppressionCosts
def populate_suppression_costs():
    with open ('suppression_costs.csv', 'r') as f:
        reader = csv.reader(f, )
        columns = next(reader)
        print("\n\n\n-----------Populating SuppressionCosts-------------\n")


        for data in reader:
            query = 'insert into SuppressionCosts({0})'

            query = query.format(','.join(columns), ','.join('?' * (len(columns) - 1)))

            col = str(data[0])
            for i in range(len(data)-1):
                if type(data[i+1]) == type('string'):
                    col = col + ",'" + str(data[i + 1]) + "'"
                else:
                    col = col + "," + str(data[i+1])
            query = query + f' values ({col});'
            print(query)

            curs.execute(query)
        curs.commit()



