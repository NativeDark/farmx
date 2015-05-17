import sys
import MySQLdb

def main () :
  file = open("list.txt",'r')
  db = MySQLdb.connect("localhost","root","","weather" ) #address,username,password,databasename
  cursor = db.cursor()
  cursor.execute("DROP TABLE IF EXISTS WEATHER")
  sql = """CREATE TABLE WEATHER (
         ID INT NOT NULL,
         NM  CHAR(20) NOT NULL,
         LAT FLOAT(12,8),
         LON FLOAT(12,8),  
         COUNTRYCODE CHAR(3) )"""
  cursor.execute(sql)
  count = 0
  for line in file:
    if count == 0:
      count = count + 1
      continue
    data = line.split('\t')
    #if data[4] == 'IN\n':  #Removed coz list of all cities might be helpful later
    cursor.execute('insert into WEATHER values("%d", "%s","%f","%f","%s")' % \
           (int(data[0]), data[1], float(data[2]), float(data[3]), data[4].replace('\n','')))
  cursor.execute('COMMIT')
  db.close()

if __name__ == '__main__':
  main()
