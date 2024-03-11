import os
with open("db.sql", "r") as f:
    data= f.read().replace("`", "")
    querys = [i.replace("\n", "") for i in data.split("\n\n")]

from MySQLdb import _mysql
 
db=_mysql.connect(host=os.getenv("HOST"), user=os.getenv("USER"),
                  password=os.getenv("PASSWORD"), database=os.getenv("DATABASE"))
 
def start_db():
    for i in querys:
        db.query(i)

start_db()
try:
    start_db()
    raise("Database is saved")
except Exception as e:
    print("Error occurs", e)