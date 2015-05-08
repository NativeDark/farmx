import sys
import urllib2
import xml.etree.ElementTree as ET
def main():
  # print 'getting all data'
  file = urllib2.urlopen("http://api.openweathermap.org/data/2.5/forecast?q=Delhi&mode=xml&cnt=16")
  data = file.read()
  file.close()
  # print data
  root = ET.fromstring(data)
  for dte in root.findall('location'):
    print dte.find('name').text
    print dte.find('country').text
  for dte in root.iter('temperature'):
    hold =  dte.attrib
    print hold['min'], hold['max'], hold['value']

if __name__ == '__main__':
  main()
