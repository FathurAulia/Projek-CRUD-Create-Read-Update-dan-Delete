import sqlite3 as sql

def main():
    try: 
        db = sql.connect('TelefonDefteri.db')
        cur = db.cursor()
        tablequery = "CREATE TABLE USER (ID INT, Nama TEXT, Nama Keluarga TEXT, Kota TEXT, TelePon TEXT, Email TEXT)"

        cur.execute(tablequery)
        print("Table Created Succesfully")

    except sql.Error as e:
        print("There is a table or an error has occurred")

    finally:
        db.close()
        
if __name__ == "__main__":
    main()