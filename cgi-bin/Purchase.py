#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import csv
import cgi
import cgitb
cgitb.enable()

def generateError(): 
	print "Content-Type: text/html;charset=utf-8"
	print
	print """
	<!doctype html>
	<html>
	<head>
	<title>Error</title>
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

def generateBill():
	print "Content-Type: text/html;charset=utf-8"
	print
	print """
	<!doctype html>
	<html>
	<head>
	<title>Bill</title>
	<style type="text/css"></style>
	</head>
	<body style="color:black; font-family:helvetica;">
	<div style="float:left; width:100%;">
	<div style="text-align:center;
	margin:0 auto;
	width:40%;">
	<body>"""
	mylist = ["retriever", "labrador", "pug", "pitbull"]
	total = 0
	print """<table>"""	
	with open('../Inventory.csv', 'rt') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar=' ')
		for row in spamreader:
			'''if gotPuppy(row[0], mylist) = True:
				print """<tr><td>""" + true + """</td></tr>"""'''
			print """<tr><td>""" + mylist[0] + """</td><td>x""" + str(row[1]) + """</td><td>$""" + str(row[2]) + """</td></tr>"""
			total = total + int(row[1])*int(row[2])
	print """<tr><td>	</td><td>Total</td><td>$""" + str(total) + """</td></tr>"""
	print """</table>
	</body>
	</html>"""



"""def gotPuppy(str, list):
	yn = False	
	for var in list:
		if var = str:
			yn = True
	return yn"""


"""form = cgi.FieldStorage()

liuser = form.getfirst("username").upper()


with open('../Members.csv', 'rt') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar=' ')
	print "Content-Type: text/plain;charset=utf-8"
	print	
	for row in spamreader:
		print row[0])"""


'''txt = open("../LoggedIn.csv", 'r')

print "Content-Type: text/plain;charset=utf-8"
print
print txt.read()'''

generateBill()



