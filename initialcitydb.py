import sys
import MySQLdb
import string

def main () :
  file = open("list.txt",'r')
  db = MySQLdb.connect("localhost","root","","weather" ) #address,username,password,databasename
  cursor = db.cursor()
  sql = """SELECT nm FROM  WEATHER where countrycode = 'IN'"""
  cursor.execute(sql)
  data = cursor.fetchall()
  #print string.ascii_uppercase
  for nm in data :
    #print nm[0]
    hold = ''.join(e for e in nm[0] if e.isalnum())
    hold = hold.lower()
    cursor.execute('drop table if exists %s' % \
                  hold)
    cursor.execute('create table %s (date date, code int, prediction char(50),cdate date)' % \
                  hold) 
  #for row in data:
    #cursor.execute('DROP TABLE IF EXISTS "%s"' % \
    #               (row[1].replace(' ','')))
    #cursor.execute('create table "%s"(date date,code int, prediction char(30))' % \
    #               (row[1].replace(' ','')))
    #hold = row[1]
    #cursor.execute('drop table if exists %s ' % \
    #       (row[1].replace(' ','')))
    #cursor.execute('create table %s (dte char(10), code int, prediction char(30))' % \
    #       (row[1].replace(' ','')))
  cursor.execute('COMMIT')
  db.close()

if __name__ == '__main__':
  main()
