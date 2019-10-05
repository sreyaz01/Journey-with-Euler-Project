import pandas as pd #to reading the csv files 
import sqlalchemy #to connecting pythone with database
from os import path 


df = pd.read_csv(path.join('Region Temperature Reports', 'Aberdeen.csv')) 
df['date'] = pd.to_datetime(df['date']) #converting datetime formate from str to date type 
print(df.dtypes) #showing typeso= of data
print(df.head(10)) #to show first 10 rows from csv file
print(df.tail(10)) #to show last 10 rows from csv file

#syntax for creating a connection with database 'variable=sqlalchemy.create_engine('postgresql+psycopg2://username:password@server_adress/db_name
engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/elliot_raju') #creating a conncection with database server

df.to_sql('weather_data', con=engine, if_exists = 'append') #pushing file on server 


