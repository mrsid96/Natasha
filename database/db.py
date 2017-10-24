# Turn on debug mode.
import cgitb
cgitb.enable()
from datetime import datetime, date, time
# Print necessary headers.
print("Content-Type: text/html")
print()

# Connect to the database.
import pymysql
conn = pymysql.connect(
    db='vibe',
    user='root',
    passwd='',
    host='localhost')
c = conn.cursor()

d = date(2017,01,13)
t = time(15,33,00)
da = datetime.combine()
# Insert some example data.
c.execute("INSERT INTO remalrm VALUES ('Event','"+da+"')")
conn.commit()

# Print the contents of the database.
c.execute("SELECT * FROM remalrm where time = (select min(time) from remalrm)" )
print([(r[0], r[1] ) for r in c.fetchall()])
