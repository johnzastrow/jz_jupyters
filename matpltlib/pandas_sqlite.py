# SQLite dataset
# We create a simple dataset using this code:

import sqlite3 as lite
import sys
import pandas as pd

# Don't create the database if it exists. Uncomment the sections below if it doesn't
# create the database. Uncomment below.
# con = lite.connect('population.db')
 
# insert some data. Uncomment below.
# with con:
#     cur = con.cursor()    
#     cur.execute("CREATE TABLE Population(id INTEGER PRIMARY KEY, country TEXT, population INT, center_lat real, center_long real)")
#     cur.execute("INSERT INTO Population VALUES(NULL,'Germany',81197537, 48.77710549, 9.11677075)")
#     cur.execute("INSERT INTO Population VALUES(NULL,'France', 66415161, 48.91291265, 2.21997772)")
#     cur.execute("INSERT INTO Population VALUES(NULL,'Hungary', 46439864, 47.52549896, 19.04276840)")
#     cur.execute("INSERT INTO Population VALUES(NULL,'Italy', 60795612, 42.03804167, 12.50358686)")
#     cur.execute("INSERT INTO Population VALUES(NULL,'Spain', 46439864, 40.36413496, -3.61373196)")

# Sqlite to Python Panda Dataframe
# An SQL query result can directly be stored in a panda dataframe:

# connect to the database
conn = lite.connect('population.db')
# query some data
query = "SELECT country FROM Population WHERE population > 50000000;"
# load the data into a dataframe
df = pd.read_sql_query(query,conn)
# loop over the data and print
for country in df['country']:
    print(country)


# from https://www.dataquest.io/blog/python-pandas-databases/

print("")
print("-----------------------------")
print("")

# Once we have a Connection object, we can then create a Cursor object. Cursors allow us to execute SQL queries against a database:

cur = conn.cursor()
cur.execute("select * from Population limit 5;")

# You may have noticed that we didn’t assign the result of the above query to a variable. 
# This is because we need to run another command to actually fetch the results. 
# We can use the fetchall method to fetch all of the results of a query:

results = cur.fetchall()
print(results)

# As you can see, the results are formatted as a list of tuples. Each tuple corresponds to a row in the database that we accessed. 
# Before we move on, it’s good practice to close Connection objects and Cursor objects that are open. 
# This prevents the SQLite database from being locked. When a SQLite database is locked, you may be 
# unable to update the database, and may get errors. We can close the Cursor and the Connection like this:

cur.close()
conn.close()