import urllib, urllib2
import lxml.etree as ET

PARSE_ADDRESS = "http://regdili.hf.ntnu.no:8081/malgram/rest/parse"

def parse(sentence):
  request = {"statement" : sentence, "client" : "crabble", "readings" : 25}
  request_address = PARSE_ADDRESS + "?" + urllib.urlencode(request)
  response = urllib2.urlopen(request_address).read()
  return ET.tostring(ET.fromstring(response), pretty_print = True)


with open('nob_news_2013_1M-sentences.txt', 'r') as datafile:
  for i, line in enumerate(datafile):
    if i == 674313:
      sentence = line.strip().split('\t')[1]
      with open(str(i) + '.xml', 'w') as outfile:
        outfile.write(parse(sentence))
