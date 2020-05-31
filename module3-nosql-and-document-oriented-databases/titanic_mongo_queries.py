# app/mongo_queries.py

import pymongo
import os
import pandas as pd
import json

# from dotenv import load_dotenv

# load_dotenv()

# DB_USER = os.getenv("DB_USER", default="MONGO OOPS")
# DB_PASSWORD = os.getenv("DB_PASSWORD", default="MONGO OOPS")
# CLUSTER_NAME = os.getenv("CLUSTER_NAME", default="MONGO OOPS")

DB_USER = 'joemac'
DB_PASSWORD = 'WnpPTBG3lyhJ2bXT'
CLUSTER_NAME = 'cluster0-udrnh'

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)
print("----------------")
print(dir(client))

print("----------------")
print('DB NAMES', client.list_database_names())

db = client.ilya_database
print("----------------")
print("DB:", type(db), db)

CSV_FILEPATH = os.path.join(os.path.dirname(__file__), 'data', 'titanic.csv')
df_titanic = pd.read_csv(CSV_FILEPATH)
str_titanic = df_titanic.to_json()
dict_titanic = json.loads(str_titanic) 

collection_name = 'titanic_csv'
collection = db[collection_name]
print("dict_titanic tyoe", type(dict_titanic))
collection.insert_one(dict_titanic)

results = collection.find({})
for result in results:
    print(result)