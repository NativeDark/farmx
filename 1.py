import sys
import urllib2
def main():
  print 'getting all data'
  file = urllib2.urlopen("http://api.openweathermap.org/data/2.5/weather?q=London&mode=xml")
  data = file.read()
  file.close()
  print data

if __name__ == '__main__':
  main()
