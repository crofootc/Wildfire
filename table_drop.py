import pyodbc
import os

# Connecting to the database
connection_string = f'Driver={{ODBC Driver 13 for SQL Server}};Server=stairway.usu.edu,1433;Database=codycrofoot;Uid={os.environ["SQLUserName"]};Pwd={os.environ["SQLPASSWORD"]}'
conn = pyodbc.connect(connection_string, autocommit=True)
print(conn)
curs = conn.cursor()

# Drop the Tables

curs.execute(
    '''
    DROP TABLE BigFires;
    DROP TABLE TotalFires;
    DROP TABLE HumanFireAcres;
    DROP TABLE HumanFireNum;
    DROP TABLE LightningFireAcres;
    DROP TABLE LightningFireNum;
    DROP TABLE SuppressionCosts;    
    '''
)

