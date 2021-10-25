import sqlite3


def sql_database():
	conn = sqlite3.connect('db.sqlite3')
	conn.execute('''CREATE TABLE Stocks_db
	(id				INTEGER NOT NULL UNIQUE,
	SYMBOL			STRING NOT NULL UNIQUE,
	HEXIMG			STRING NOT NULL,
	CLOSE			REAL NOT NULL,
	OPEN			REAL NOT NULL,
	LOW				REAL NOT NULL,
	HIGH			REAL NOT NULL,
	ADJCLOSE		REAL NOT NULL,
	DATE			BLOB NOT NULL,
	PRIMARY KEY("id","SYMBOL")
	);''')
	conn.commit()

	conn.close()
