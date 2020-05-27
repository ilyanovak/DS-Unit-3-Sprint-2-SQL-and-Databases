import psycopg2
from psycopg2.extras import DictCursor
import pandas
import os

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')

from dotenv import load_dotenv
load_dotenv()

connection = psycopg2.connect(
    dbname=os.getenv('DB_NAME'), 
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASS'), 
    host=os.getenv('DB_HOST')
    )

# connection = psycopg2.connect(
#     dbname=DB_NAME, 
#     user=DB_USER,
#     password=DB_PASS, 
#     host=DB_HOST
#     )
print(connection)
cursor = connection.cursor(cursor_factory=DictCursor)
print(cursor)

query1 = "CREATE TABLE IF NOT EXISTS titanic (Survived INT, Pclass INT, Name VARCHAR(20), Sex VARCHAR(20), Age INT, Siblings_Spouses_Aboard INT, Parents_Children_Aboard INT, Fare FLOAT);"
cursor.execute(query1)
connection.commit()

from sqlalchemy import create_engine
sql_url = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
engine = create_engine(sql_url)
CSV_FILEPATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'titanic.csv')
df = pandas.read_csv(CSV_FILEPATH)
# print(df)
df.to_sql('titanic', engine, if_exists='replace')
connection.commit()

query3 = 'SELECT * FROM titanic;'
cursor.execute(query3)
result = cursor.fetchall()
print(result)

cursor.close()
connection.close()