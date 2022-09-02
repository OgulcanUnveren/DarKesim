import sqlite3

connection = sqlite3.connect('asskicker.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS logs(id integer PRIMARY KEY,pid integer NOT NULL,ProcessName text NOT NULL,Time text NOT NULL,Connections text NOT NULL);''')
cursor.execute('''CREATE TABLE IF NOT EXISTS browserhistory(id integer PRIMARY KEY,wholeconn text NOT NULL,raddr text NOT NULL,Time text NOT NULL,rport text NOT NULL);''')
connection.commit()
connection.close()
