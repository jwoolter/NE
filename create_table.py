import sqlite3

def create_table(db_name,table_name,sql):
                print("in create func")
                with sqlite3.connect(db_name) as db:
                    cursor = db.cursor()
                    cursor.execute("select name from sqlite_master where name=?", (table_name,))
                    result = cursor.fetchall()
                    keep_table = True
                    if len(result) == 1:
                        response = input("The table {0} already exists, do you wish to recreate it (y/n): ".format(table_name,))
                        if response == "y":
                            keep_table = False
                            print("The {0} table will be recreated - all exisitng data will be deleted".format(table_name))
                            cursor.execute("drop table if exists {0}".format(table_name))
                            db.commit
                        else:
                            print("the existing table was kept")
            
                    else:
                        keep_table = False
                        print("no current table")
                    if not keep_table:
                        cursor.execute(sql)
                        print("executed SQL")
                        db.commit()

db_name = "test.db" 
sql = """create table Test1
(PlayerID integer,
PlayerName text,
Hand float,
currency integer,
primary key(PlayerID))"""
            
create_table("test.db","Test", sql)