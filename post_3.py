#!/usr/bin/python 
#!coding:utf-8
from html.parser import HTMLParser
from urllib.parse import urlparse
from urllib import request
import urllib.error
import http.cookiejar
import string
import re
hosturl = 'http://10.17.0.3/cgi-bin/ace_web_auth.cgi'
posturl = 'http://10.17.0.3/cgi-bin/ace_web_auth.cgi'
CookieJar = http.cookiejar.CookieJar()
Cookie_support = urllib.request.HTTPCookieProcessor(CookieJar)
opener = urllib.request.build_opener(Cookie_support)
urllib.request.install_opener(opener)
h = urllib.request.urlopen(hosturl)
headers = {     'Origin' : 'http://10.17.0.3',
      'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
      'Referer' : 'http://10.17.0.3/login.php'}
postData = {'username' : '1609060320',
      'userpwd' : '123456',
      'login' : '登 录',
      'orig_referer' : ''
			}
postData = urllib.parse.urlencode(postData).encode('utf-8')
request = urllib.request.Request(posturl, postData, headers)
response = urllib.request.urlopen(request)
print (request)
print ('=======================================================')
print(response.read().decode('utf-8'))