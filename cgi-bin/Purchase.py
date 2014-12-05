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
	<title>Not Logged In</title>
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

def generateBill(username, n):
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
	print """<h3>Hello, """ + str(username) + """.  Please verify your bill below.</h3>"""	
	print """<table>"""
	print """<thead> <td>Puppies ordered</td> <td>Number ordered</td> <td>Unit Rental Price</td></thead>"""	
	with open('../data/Inventory.csv', 'rt') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar=' ')
		for row in spamreader:
			print """<tr><td>""" + str(mylist[0]) + """</td><td>x""" + str(n) + """</td><td>$""" + str(row[2]) + """</td></tr>"""
			total = total + int(n)*int(row[2])
	print """<tr><td>	</td><td>Total</td><td>$""" + str(total) + """</td></tr>"""
	print """</table>
	</body>
	</html>"""

def getStock(pup):
	with open('../data/Inventory.csv', 'rt') as cfile:
		sreader = csv.reader(cfile, delimiter=',', quotechar=' ')
		for m in sreader:
			if pup == m[0]:
				return int(m[1])

def getPrice(pupname):
	with open('../data/Inventory.csv', 'rt') as csfile:
		freader = csv.reader(csfile, delimiter=',', quotechar=' ')
		for puppy in freader:
			if pupname == puppy[0]:
				return int(puppy[2])

form = cgi.FieldStorage()

liuser = form.getfirst("username")
ofeach = form.getfirst("Dalmation")

if liuser != "":
	isLogged = False
	with open('../data/LoggedIn.csv', 'rt') as logfile:
		logreader = csv.reader(logfile, delimiter=',', quotechar=' ')
		for logged in logreader:
			if liuser == logged[0]:
				isLogged = True
	if isLogged:
		generateBill(liuser, ofeach)
	else:
		generateError()
else:
	generateError()





