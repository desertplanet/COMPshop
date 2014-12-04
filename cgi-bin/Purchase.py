#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cgi
import cgitb
cgitb.enable()

print "Content-Type: text/html;charset=utf-8"
print

def generateError(): 

	print """
<!doctype html>
<html>
<head></head>
<body>
<p>Since you are not logged in, your order could not be processed.</p>
<p>Please log in by clicking <a href = ../login.html>here</a>.</p>
</body>
</html>"""


generateError()
