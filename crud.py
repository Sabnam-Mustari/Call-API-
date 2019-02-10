# https://www.sqlrelease.com/connecting-python-3-to-sql-server-2017-using-pyodbc
import pyodbc as db
con = db.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=.;Trusted_Connection=yes;DATABASE=DBTest')
cur = con.cursor()


class crud:
  def __init__(self, User_id, ID, Title, Body):
    self.User_id = User_id
    self.ID = ID
    self.Title = Title
    self.Body = Body

  @classmethod
  def insert(self, json_data):
      con = db.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=.;Trusted_Connection=yes;DATABASE=DBTest')
      cur = con.cursor()
      qry = '''INSERT INTO dbo.tbl_Api
              (user_ID, id, title, status)
              VALUES(?, ?, ?, ?)
              '''
      for i, item in enumerate(json_data):
          User_id = item.get('userId')
          ID = item.get('id')
          Title = item.get('title')
          Body = item.get('body')
          obj = crud(User_id, ID, Title, Body)
          param_values = [obj.User_id, obj.ID, obj.Title, obj.Body]
          cur.execute(qry, param_values)
      print('{0} row inserted successfully.'.format(cur.rowcount))
      cur.commit()  # Use this to commit the insert operation
      cur.close()
      con.close()

  @classmethod
  def read(self):
      con = db.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=.;Trusted_Connection=yes;DATABASE=DBTest')
      cur = con.cursor()
      qry = '''select * from dbo.tbl_Api'''
      cur.execute(qry)
      records = cur.fetchall()
      mylist = []
      for row in records:
          User_id = row[0]
          ID =  row[1]
          Title = row[2]
          Body = row[3]
          #print("userId = ", row[0], "ID = ", row[1],"Title  = ", row[2],"Body  = ", row[3], "\n")
          obj = crud(User_id, ID, Title, Body)
          if obj.ID < 3:
              param_values = (obj.User_id, obj.ID, obj.Title, obj.Body)
              mylist.append(param_values)
      print("Mylist:", mylist)
      cur.commit()  # Use this to commit the insert operation
      cur.close()
      con.close()
  @classmethod
  def update(self):
      con = db.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=.;Trusted_Connection=yes;DATABASE=DBTest')
      cur = con.cursor()
      # SELECT all rows from employee table
      qry = '''UPDATE dbo.tbl_Api
              SET user_ID = ?, id = ?, title =? 
              WHERE status = ?
              '''
      param_values = [0,0, 'None', '0']
      cur.execute(qry, param_values)

      print('{0} row updated successfully.'.format(cur.rowcount))

      cur.commit()  # Use this to commit the update operation
      cur.close()
      con.close()

  @classmethod
  def delete(self):
      con = db.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=.;Trusted_Connection=yes;DATABASE=DBTest')
      cur = con.cursor()
      # SELECT all rows from employee table
      qry = '''DELETE tbl_Api
              WHERE title = ?
              '''
      param_values = ['sed ab est est']
      cur.execute(qry, param_values)
      print('{0} row deleted successfully.'.format(cur.rowcount))
      cur.commit()  # Use this to commit the update operation
      cur.close()
      con.close()
