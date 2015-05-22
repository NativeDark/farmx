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
    table = ''.join(e for e in nm[0] if e.isalnum())
    table = table.lower()
    try:
      file = urllib2.urlopen(str)
    except urllib2.HTTPError, err:
      if err.code >= 500:
        file = urllib2.urlopen(str)
    data = file.read()
    file.close()
    try:
      root = ET.fromstring(data)
    except ET.ParseError, code:
      print 'ParseError in reading ',nm[0]
      file = urllib2.urlopen(str)
      data = file.read()
      file.close()
    city= root[0][0].text
    print 'Batch Running for City: ',city,' table :',table
    for child in root.findall('forecast'):
      for sym in child.findall('time'):
        for c2 in sym.findall('symbol'):
          #print c2.get('number'), c2.get('name'), sym.get('day')
          #cursor.execute('insert into  values ("2015-12-12",200,"challl","2015-12-12")')
          cursor.execute('insert into %s values ("%s", %d, "%s", CURDATE()) ' % \
                          (table, sym.get('day'), int(c2.get('number')), c2.get('name') ))

if __name__ == '__main__':
  main()
