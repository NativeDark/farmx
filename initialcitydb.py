import sys
import MySQLdb

def main () :
  file = open("list.txt",'r')
  db = MySQLdb.connect("localhost","root","","weather" ) #address,username,password,databasename
  cursor = db.cursor()
  sql = """SELECT * FROM  WEATHER where countrycode = 'IN'"""
  cursor.execute(sql)
  data = cursor.fetchall()
  for row in data:
    #cursor.execute('DROP TABLE IF EXISTS "%s"' % \
    #               (row[1].replace(' ','')))
    #cursor.execute('create table "%s"(date date,code int, prediction char(30))' % \
    #               (row[1].replace(' ','')))
    cursor.execute('drop table if exists %s ' % \
           (row[1].replace(' ','')))
    cursor.execute('create table %s (dte char(10), code int, prediction char(30))' % \
           (row[1].replace(' ','')))
  cursor.execute('COMMIT')
  db.close()

if __name__ == '__main__':
  main()
