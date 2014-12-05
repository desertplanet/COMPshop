#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import csv
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

liuser = form.get("username")

def generateError(): 
	print "Content-Type: text/html;charset=utf-8"
	print
	print """
	<!doctype html>
	<html>
	<head>
	<title>catalogue</title>
	<style type="text/css"></style>
	</head>
	<body style="color:black; font-family:helvetica;">
	<div style="float:left; width:100%;">
	<div style="text-align:center;
	margin:0 auto;
	width:40%;">
	<body>
	<p>Since you are not logged in, your order could not be processed.</p>
	<p>Please log in by clicking <a href = ../login.html>here</a>.</p>
	</body>
	</html>"""

if liuser = "":
	generateError()
else:
	with open('LoggedIn.csv', 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for row in spamreader:
			print ', '.join(row)
