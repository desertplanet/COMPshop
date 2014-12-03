#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging	
import webbrowser
import cgitb
cgitb.enable()

print "Content-Type: text/plain;charset=utf-8"
print

def generateError():
	f = open('error.html','w')

	message = """<html>
	<head></head>
	<body>
	<p>Since you are not logged in, your order could not be processed.</p>
	<p>Please log in by clicking <a href = ../login.html>here</a>.</p>
	</body>
	</html>"""

	f.write(message)
	f.close()
	url = " cgi-bin/error.html"	
	webbrowser.open(url)

webbrowser.open('www.google.com')
generateError()	
