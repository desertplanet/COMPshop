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
	print """<h3>Hello, """ + str(username) + """.  Please verify your bill below.</h3>"""	
	print """<table>"""
	print """<thead> <td>Puppies ordered</td> <td>Number ordered</td> <td>Unit Rental Price</td></thead>"""	
	total = 0
	while len(n) > 0:
		pname = n.pop()
		pnum = n.pop()
		punit = n.pop()
		print """<tr><td>""" + str(pname) + """</td><td>x""" + str(pnum) + """</td><td>$""" + str(punit) + """</td></tr>"""
		total = total + int(pnum)*int(punit)
	print """<tr><td>	</td><td>Total</td><td>$""" + str(total) + """</td></tr>"""
	print """</table>
	</body>
	</html>"""

def removeInventory(lcpy):
	with open('../data/Inventory.csv', 'wt') as refile:
		rewriter = csv.writer(refile, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
		while len(lcpy) > 0:
			uname = lcpy.pop()
			ustock = lcpy.pop()
			uprice = lcpy.pop()
			rewriter.writerow([uname,ustock,uprice])

def getPrice(pupname):
	with open('../data/Inventory.csv', 'rt') as csfile:
		freader = csv.reader(csfile, delimiter=',', quotechar=' ')
		for puppy in freader:
			if pupname == puppy[0]:
				return int(puppy[2])

form = cgi.FieldStorage()
liuser = form.getfirst("username")
mygiantlist = []
listcopy = []

with open('../data/Inventory.csv', 'rt') as cofile:
	coreader = csv.reader(cofile, delimiter=',', quotechar=' ')
	for p in coreader:
		checkme = form.getfirst(str(p[0]))
		if checkme == "true":
			pupnum = str(p[0]) + 'num'
			numtoget = form.getfirst(pupnum)
			if int(p[1]) >= int(numtoget):
				mygiantlist.append(str(p[0]))
				mygiantlist.append(numtoget)
				price = getPrice(str(p[0]))
				mygiantlist.append(price)
				listcopy.append(str(p[0]))
				newstock = int(p[1]) - int(numtoget)
				listcopy.append(newstock)
				listcopy.append(price)
			else:
				mygiantlist.append(str(p[0]))
				mygiantlist.append(p[1])
				price = getPrice(str(p[0]))
				mygiantlist.append(price)
				listcopy.append(str(p[0]))
				listcopy.append(0)
				listcopy.append(price)
		else:
			listcopy.append(str(p[0]))
			listcopy.append(int(p[1]))
			newprice = getPrice(str(p[0]))
			listcopy.append(newprice)

mygiantlist.reverse()
listcopy.reverse()

if liuser != "":
	isLogged = False
	with open('../data/LoggedIn.csv', 'rt') as logfile:
		logreader = csv.reader(logfile, delimiter=',', quotechar=' ')
		for logged in logreader:
			if liuser == logged[0]:
				isLogged = True
	if isLogged:
		generateBill(liuser, mygiantlist)
		removeInventory(listcopy)
	else:
		generateError()
else:
	generateError()





