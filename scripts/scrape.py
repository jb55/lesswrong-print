import sys
import os
import urllib2

def extract_article(data):
  start = data.find("<!-- .meta -->")
  end = data.find("<!-- .content -->")
  return data[start:end]

def scrape(url, n, t):
  print "(%d/%d) Downloading" % (n, t), url
  data = urllib2.urlopen(url).read()
  extracted = extract_article(data)
  endpart = filter(lambda e: e != '', url.split('/'))[-1]
  fname = 'out/' + endpart + '.html'
  f = open(fname, 'w')
  f.write(extracted)
  f.close()

def main():
  urls = sys.argv[1:]
  t = len(urls)
  i = 1
  for url in urls:
    scrape(url, i, t)
    i = i + 1

if __name__ == "__main__":
  main()
