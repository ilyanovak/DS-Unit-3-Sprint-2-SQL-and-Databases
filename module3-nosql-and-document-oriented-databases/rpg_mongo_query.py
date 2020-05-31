# app/mongo_queries.py

import pymongo
import os
import pandas as pd
import json

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

collection_name = 'rpg'
collection = db[collection_name]

rpg_json_list = [
    'armory_item',
    'armory_weapon', 
    'charactercreator_character',
    'charactercreator_character_inventory',
    'charactercreator_cleric',
    'charactercreator_fighter',
    'charactercreator_mage',
    'charactercreator_necromancer',
    'charactercreator_thief']

def Convert(lst): 
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)} 
    return res_dct 

for filename in rpg_json_list:
    print('RPG Table:', filename)
    JSON_FILEPATH = os.path.join(os.path.dirname(__file__), 'data', filename+'.json')
    df_rpg = pd.read_json(JSON_FILEPATH)
    str_rpg = df_rpg.to_json()
    dict_rpg = json.loads(str_rpg)
    collection.insert_one(dict_rpg)