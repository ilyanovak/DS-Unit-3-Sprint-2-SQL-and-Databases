import os
import sqlite3

QUESTION1 = '\nHow many total Characters are there?'
QUESTION2 = '\nHow many of each specific subclass?'
QUESTION3 = '\nHow many total Items?'
QUESTION45 = '\nHow many of the Items are weapons? How many are not?'
QUESTION6 = '\nHow many Items does each character have? (Return first 20 rows)'
QUESTION7 = '\nHow many Weapons does each character have? (Return first 20 rows)'
QUESTION8 = '\nOn average, how many Items does each Character have?'
QUESTION9 = '\nOn average, how many Weapons does each character have?'

QUERY1 = 'SELECT count(distinct character_id) FROM charactercreator_character'
QUERY2 = 'SELECT (SELECT count(distinct character_ptr_id) FROM charactercreator_cleric) AS cleric_count, (SELECT count(distinct character_ptr_id) FROM charactercreator_fighter) AS fighter_count, (SELECT count(distinct character_ptr_id) FROM   charactercreator_mage) AS mage_count, (SELECT count(distinct mage_ptr_id) FROM charactercreator_necromancer) AS necromancer_count, (SELECT count(distinct character_ptr_id) FROM charactercreator_thief) AS thief_count'
QUERY3 = 'SELECT count(item_id) FROM armory_item AS item_count'
QUERY4 = 'SELECT count(distinct item_id) FROM armory_item INNER JOIN armory_weapon ON armory_item.item_id = armory_weapon.item_ptr_id'
QUERY5 = 'SELECT count(distinct item_id) FROM armory_item LEFT JOIN armory_weapon ON armory_item.item_id = armory_weapon.item_ptr_id WHERE armory_weapon.item_ptr_id IS NULL'
QUERY6 = 'SELECT count(item_id) FROM charactercreator_character_inventory GROUP BY character_id LIMIT 20'
QUERY7 = 'SELECT character_id, count(item_id) FROM charactercreator_character_inventory INNER JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id GROUP BY character_id LIMIT 20'
QUERY8 = 'SELECT avg(item_counts) FROM (SELECT count(item_id) as item_counts FROM charactercreator_character_inventory GROUP BY character_id)'
QUERY9 = 'SELECT AVG(weapon_counts) FROM (SELECT count(item_id) as weapon_counts FROM charactercreator_character_inventory INNER JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id GROUP BY character_id)'

def execute_query(QUERY_STRING):
    conn = sqlite3.connect('rpg_db.sqlite3')
    curs = conn.cursor()
    query = 'SELECT COUNT(*) FROM armory_item;'
    curs.execute(QUERY1)
    query_result = curs.execute(QUERY_STRING).fetchall()
    print(query_result)


# def execute_query(QUERY_STRING):
    # DB_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.sqlite3")
    # connection = sqlite3.connect(DB_FILEPATH)
    # connection.row_factory = sqlite3.Row
    # cursor = connection.cursor()
    # query_result2 = cursor.execute(QUERY2)
    # query_result2 = cursor.execute(QUERY2).fetchall()
    # print(query_result2['cleric_count'])

if __name__ == "__main__":
    print(QUESTION1)
    execute_query(QUERY1)

    print(QUESTION2)
    execute_query(QUERY2)

    print(QUESTION3)
    execute_query(QUERY3)

    print(QUESTION45)
    execute_query(QUERY4)
    execute_query(QUERY5)

    print(QUESTION6)
    execute_query(QUERY6)

    print(QUESTION7)
    execute_query(QUERY7)

    print(QUESTION8)
    execute_query(QUERY8)

    print(QUESTION9)
    execute_query(QUERY9)