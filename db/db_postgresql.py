import psycopg2

def createtable():
    # connect to database in postgresql
    conn = psycopg2.connect("dbname='data2' user='postgres' password='postgres' port='5432' host='localhost'")
    # cursor
    cur = conn.cursor()
    # execution - create a table named 'data' with columns rollno(int), name(string), marks (float)
    cur.execute("CREATE TABLE data(rollno INTEGER, name TEXT, marks REAL)")
    # commit
    conn.commit()
    # close
    conn.close()

def insert(roll,nam,mark):
    conn = psycopg2.connect("dbname='data2' user='postgres' password='postgres' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("INSERT INTO data VALUES(%s,%s,%s)", (roll, nam, mark))
    conn.commit()
    conn.close()

### VISUALISING DATA ###
def view():
    conn = psycopg2.connect("dbname='data2' user='postgres' password='postgres' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM data")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

### DELETING DATA ###
def delete(roll):
    conn = psycopg2.connect("dbname='data2' user='postgres' password='postgres' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("DELETE FROM data WHERE rollno=%s", (roll,))
    conn.commit()
    conn.close()

### UPDATING DATA ###
def update(roll,nam,mark):
    conn = psycopg2.connect("dbname='data2' user='postgres' password='postgres' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("UPDATE data SET name=%s,marks=%s WHERE rollno=%s", (nam,mark,roll))
    conn.commit()
    conn.close()

print(view())
update(1,'1st',50)
print(view())