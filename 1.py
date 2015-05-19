import sys
import urllib2
import xml.etree.ElementTree as ET
import MySQLdb

def main():
  string = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=CITY&mode=xml&cnt=16'
  db = MySQLdb.connect("localhost","root","","weather" ) #address,username,password,databasename
  cursor = db.cursor()
  sql = """SELECT nm FROM  WEATHER where countrycode = 'IN'"""
  cursor.execute(sql)
  data = cursor.fetchall()
  for nm in data:
    hold = nm[0].replace(' ','%20')
    str = string.replace('CITY',hold)
    table = chr(ord(hold[0]))
    file = urllib2.urlopen(str)
    data = file.read()
    file.close()
    root = ET.fromstring(data)
    city= root[0][0].text
    print city
    for child in root.findall('forecast'):
      for sym in child.findall('time'):
        for c2 in sym.findall('symbol'):
          #print c2.get('number'), c2.get('name'), sym.get('day')
          cursor.execute('insert into %c values ("%s","%s",%d,"%s") ' % \
                          (table,nm[0],sym.get('day'),int(c2.get('number')),c2.get('name')))
          cursor.execute('commit')

if __name__ == '__main__':
  main()
