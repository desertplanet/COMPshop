#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb

def generateBill():
	

def generateError():
	import webbrowser

	f = open('error.html','w')

	message = """<html>
	<head></head>
	<body>
	<p>Since you are not logged in, your order could not be processed.</p>
	<p>Please log in <a href = login.html>here</a>.</p>
	</body>
	</html>"""

	f.write(message)
	f.close()

	webbrowser.open_new_tab('helloworld.html')
	
if username == "":
	generateError()