import sqlite3

def insert_data(values):
    with sqlite3.connect("test.db") as db:
        cursor = db.cursor()
        sql = "insert into Test1(PlayerID, PlayerName, Hand ,Currency) values (?,?,?,?)"
        cursor.execute(sql,values)
        db.commit()

if __name__== "__main__":
    product = (3,"Alex", 6.4, 14)
    insert_data(product)