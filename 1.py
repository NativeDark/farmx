import sys
import urllib2
import xml.etree.ElementTree as ET
def main():
  file = urllib2.urlopen("http://api.openweathermap.org/data/2.5/forecast/daily?q=Delhi&mode=xml&cnt=16")
  data = file.read()
  file.close()
  root = ET.fromstring(data)
  print root[0][0].text
  for child in root.findall('forecast'):
    for sym in child.findall('time'):
      for c2 in sym.findall('symbol'):
        print c2.get('number'), c2.get('name'), sym.get('day')

if __name__ == '__main__':
  main()
