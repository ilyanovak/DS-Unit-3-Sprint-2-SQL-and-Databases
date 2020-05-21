import os
import sqlite3
import pandas as pd

# def execute_query(QUERY_STRING):
#     conn = sqlite3.connect('rpg_db.sqlite3')
#     curs = conn.cursor()
#     query = 'SELECT COUNT(*) FROM armory_item;'
#     curs.execute(QUERY1)
#     query_result = curs.execute(QUERY_STRING).fetchall()
#     print(query_result)

if __name__ == "__main__":
    DF_PATH = 'C:\\Users\\Ilya Novak\\Documents\\lambda\\repos\\DS-Unit-3-Sprint-2-SQL-and-Databases\\module1-introduction-to-sql\\'
    df = pd.read_csv(DF_PATH+'buddymove_holidayiq.csv')
    print(df.shape)

    conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
    curs = conn.cursor()

    QUERY = "DROP TABLE review"
    curs.execute(QUERY)

    QUERY = "CREATE TABLE review ('User Id' varchar(255),'Sports' INT,'Religious' INT,'Nature' INT,'Theatre' INT,'Shopping' INT,'Picnic' INT)"
    curs.execute(QUERY)
 
    df.to_sql('review', con=conn, if_exists='replace')

    QUERY = "SELECT * FROM review"
    curs.execute(QUERY)
    result = curs.fetchall()
    for i in result:
        print(i)

    print('\nCount how many rows you have - it should be 249!')
    QUERY = "SELECT count('User Id') FROM review"
    curs.execute(QUERY)
    result = curs.fetchall()
    print(result)

    print('\nHow many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category?')
    QUERY = "SELECT count('User Id') FROM review WHERE 'Nature' >= 100 AND 'Shopping' >= 100"
    curs.execute(QUERY)
    result = curs.fetchall()
    print(result)