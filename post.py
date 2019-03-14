#!/usr/bin/python 
#!coding:utf-8
import HTMLParser 
import urlparse 
import urllib 
import urllib2 
import cookielib 
import string 
import re 
hosturl = 'http://10.17.0.3/cgi-bin/ace_web_auth.cgi'
posturl = 'http://10.17.0.3/cgi-bin/ace_web_auth.cgi'
cj = cookielib.LWPCookieJar() 
cookie_support = urllib2.HTTPCookieProcessor(cj) 
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler) 
urllib2.install_opener(opener) 
h = urllib2.urlopen(hosturl) 
headers = {	'Origin' : 'http://10.17.0.3',
	  'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0', 
      'Referer' : 'http://10.17.0.3/login.php'} 
postData = {'username' : '1609060320', 
      'userpwd' : '123456',
      'login' : '登 录',
      'orig_referer' : ''
      } 
postData = urllib.urlencode(postData) 
request = urllib2.Request(posturl, postData, headers) 
print request 
line = '======================================================='
print line
response = urllib2.urlopen(request) 
text = response.read() 
print text