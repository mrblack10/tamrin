import sqlite3

connect = sqlite3.connect("./my-database.dp")
cursor = connect.cursor()

sql = """
    CREATE TABLE IF NOT EXISTS user (
    userId INTEGER ,
    name VARCHAR (60),
    family VARCHAR (60)
    );
"""
cursor.execute(sql)

connect.commit()
connect.close()
