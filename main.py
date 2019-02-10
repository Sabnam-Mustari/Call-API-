# https://www.sqlrelease.com/connecting-python-3-to-sql-server-2017-using-pyodbc
import requests
import pyodbc as db
from crud import *
from datetime import datetime
from threading import Timer

x=datetime.today()
# This will execute a function (eg. hello_world) in the next day at 1a.m.
#y=x.replace(day=x.day+1, hour=1, minute=0, second=0, microsecond=0)
y=x.replace(day=x.day, hour=16, minute=8, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

url_address = 'https://jsonplaceholder.typicode.com/posts'
#api_address = 'https://jsonplaceholder.typicode.com/todos/1'
#url = api_address
url = url_address
json_data = requests.get(url).json()
#print(json_data)
con = db.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=.;Trusted_Connection=yes;DATABASE=DBTest')
cur = con.cursor()
qry = '''select * from dbo.tbl_Api'''
cur.execute(qry)
records = cur.fetchall()

def main():
    crud.insert(json_data)
    crud.read()
    crud.update()
    crud.delete()
    t = Timer(secs, crud.read)
    t.start()

if __name__ == "__main__":
	main()

