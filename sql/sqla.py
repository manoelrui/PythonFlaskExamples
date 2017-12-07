#Create a sql3 database and table

#import the sqlite3 libray
import sqlite3

# Create a new database if the database doesn't already exist
conn = sqlite3.connect("new.db")

# get a cursor object used to execute sql commands
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE population (city TEXT, state TEXT, population INT) """)

# close the database connection
conn.close()
