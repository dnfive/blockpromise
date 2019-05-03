#-------------------------------------
# 			blockpromise
#	Blockchain system for promise
#-------------------------------------
# 			writed by dnfive
#-------------------------------------


import sqlite3

conn = sqlite3.connect("blockchain.db")
cursor = conn.cursor()

# Создание таблицы
# cursor.execute("""
#				CREATE TABLE blockchain(
#						id INTEGER PRIMARY KEY AUTOINCREMENT,
#						comment TEXT,
#						prev_hash TEXT
#                   )
#               """)

