import sqlite3

# 5 Steps

def createtable():
    # connection
    conn = sqlite3.connect('lite.db')
    # cursor
    cur = conn.cursor()
    # execution - create a table named 'data' with columns rollno(int), name(string), marks (float)
    cur.execute("CREATE TABLE data(rollno INTEGER, name TEXT, marks REAL)")
    # commit
    conn.commit()
    # close
    conn.close()

### INSERT DATA INTO TABLE ###
def insert(roll,nam,mark):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO data VALUES(?, ?, ?)", (roll,nam, mark))
    conn.commit()
    conn.close()

### VISUALISING DATA ###
def view():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM data")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

### DELETING DATA ###
def delete(roll):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM data WHERE rollno=?", (roll,))
    conn.commit()
    conn.close()

### UPDATING DATA ###
def update(roll,nam,mark):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("UPDATE data SET name=?,marks=? WHERE rollno=?", (nam,mark,roll))
    conn.commit()
    conn.close()

print(view())
update(2,'1st', 56)
print(view())