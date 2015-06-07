import sys
import urllib2
import xml.etree.ElementTree as ET
import MySQLdb

def main():
  db = MySQLdb.connect("localhost","root","","weather" ) #address,username,password,databasename  
  cursor = db.cursor()
  sql = "SELECT nm FROM  WEATHER where countrycode = 'IN'"
  cursor.execute(sql)
  data = cursor.fetchall()
  for nm in data:
    #Here we will call the function which will recurisvely get data
    table = gettable(nm[0])
    data = getxml(nm[0])
    root = getroot(data)
    city= root[0][0].text
    print 'Batch Running for City: ',city,' table :',table
    for child in root.findall('forecast'):
      for sym in child.findall('time'):
        for c2 in sym.findall('symbol'):
          #print c2.get('number'), c2.get('name'), sym.get('day')
          #cursor.execute('insert into  values ("2015-12-12",200,"challl","2015-12-12")')
          cursor.execute('insert into %s values ("%s", %d, "%s", CURDATE()) ' % \
                          (table, sym.get('day'), int(c2.get('number')), c2.get('name') ))

def getxml(city):
  string = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=CITY&mode=xml&cnt=16'
  hold = city.replace(' ','%20')
  str = string.replace('CITY',hold)
  try:
    file = urllib2.urlopen(str)
    data = file.read()
    file.close()
  except urllib2.HTTPError, err:
    if err.code >= 500:
      #file = urllib2.urlopen(str)
      print 'Error in:',city
      data = getxml(city)
  return data

def getroot(data):
  try:
    root = ET.fromstring(data)
  except ET.ParseError, code:
    print 'parse error:',data[0][0]
    data = getxml(city)
    root = getroot(data)
  return root

def gettable(city):
  table = ''.join(e for e in city if e.isalnum())
  table = table.lower()
  return table

if __name__ == '__main__':
  main()
