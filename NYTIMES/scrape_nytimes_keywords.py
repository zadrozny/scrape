#!/usr/local/bin/python2.7

import datetime
import re
import requests

page = requests.get('http://nytimes.com').text.encode('utf-8')

pat = '<meta name="keywords" content="(.*?)/>'

with open('nytimes_keywords.txt', 'a') as f:
    f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    f.write('\n')
	f.write(re.findall(pat, page)[0])
	f.write('\n\n')

