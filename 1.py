import sys
import urllib2
import xml.etree.ElementTree as ET
def main():
  # print 'getting all data'
  file = urllib2.urlopen("http://api.openweathermap.org/data/2.5/forecast/daily?q=Delhi&mode=xml&cnt=16")
  data = file.read()
  file.close()
  # print data
  root = ET.fromstring(data)
  #for dte in root.findall('location'):
  #  print dte.find('name').text
  #  print dte.find('country').text
  #for dte in root.iter('time'):
  #  hold =  dte.attrib
  #  print hold['day']
  #print root[0][0].text
  for child in root.findall('forecast'):
    # print child
    for sym in child.findall('time'):
      for c2 in sym.findall('symbol'):
        print c2.get('number'), c2.get('name'), sym.get('day')
    # date = child.get('day').text
    # print sym


if __name__ == '__main__':
  main()
