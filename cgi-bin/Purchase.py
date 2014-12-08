#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from random import randrange
import cgi
import cgitb
cgitb.enable()

"""
This method generates the error pages if the user is not logged in or the username
is not on the list of logged in users.
"""
def generateError(): 
	print "Content-Type: text/html;charset=utf-8"
	print
	print """
	<!doctype html>
	<html>
	<head>
	<link rel="stylesheet" type="text/css" href="../stylesheets/main.css">
	<title>Not Logged In</title>
	<style type="text/css"></style>
	</head>
	<body style="color:black; font-family:helvetica;">
	<div id = "home">
	<div id = "bill">
	<center>
	<p>Since you are not logged in, your order could not be processed.</p>
	<form name="goback2home" method="post" action="../index.html">
	<input name = "username" type = "hidden" value ="null"></input>
	<input type = "submit" value = "home"></input>
	</form>
	<form name="goback2login" method="post" action="../login.html">
	<input name = "username" type = "hidden" value ="null"></input>
	<input type = "submit" value = "log in"></input>
	</form>
	<form name="goback" method="post" action="../c.cgi">
	<input name = "username" type = "hidden" value ="null"></input>
	<input type = "submit" value = "catalogue"></input>
	</form>
	</center>
	</div>
	</div>
	</body>
	</html>"""

'''
This method generates the bill of the current logged in user.
@param username The current logged in user
@param n The list with the name, amount, and unit price of every item ordered

This generates an html page, prints a greeting to the user, generates the bill.
The checkout link, home page, catalogue page are linked at the bottom.
'''
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
	<link rel="stylesheet" type="text/css" href="../stylesheets/main.css">
	<title>Not Logged In</title>
	<style type="text/css"></style>
	</head>
	<body style="color:black; font-family:helvetica;">
	<div id = "home">
	<div id = "bill">
	<center>"""
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
	<h3>
	<form name="submit" method="post" action="generateEnd.py">
	<input name = "username" type = "hidden" value =\"""" + str(username) + """\"></input>
	<input type="submit" value="Checkout"></input>
	</form>
	</h3>
	<form name="goback2home" method="post" action="../index.html">
	<input name = "username" type = "hidden" value =\"""" + str(username) + """\"></input>
	<input type = "submit" value = "home"></input>
	</form>
	<form name="goback" method="post" action="../c.cgi">
	<input name = "username" type = "hidden" value =\"""" + str(username) + """\"></input>
	<input type = "submit" value = "catalogue"></input>
	</form>
	</center>
	</div>
	</div>
	</body>
	</html>"""

"""
This method overwrites the inventory based on the list that contains the entire new inventory.
@param lcpy The list that contains the name, new stock amount, and price of all items.
"""
def removeInventory(lcpy):
	with open('../data/Inventory.csv', 'wt') as newinvfile:
		while len(lcpy) > 0:
			uname = str(lcpy.pop())
			ustock = str(lcpy.pop())
			uprice = str(lcpy.pop())
			udescrip = str(lcpy.pop())
			rewriter = ",".join([uname,ustock,uprice,udescrip])
			writeline = str(rewriter) + "\n"
			newinvfile.write(writeline)
	newinvfile.closed

def randomRestock():
	if randrange(10) > 4:
		return randrange(3) + 1
	else:
		return 0
"""
Gets all inputs from the catalogue.html page
Gets the hidden username from the page
Creates two empty lists: one for the bill generation, one for updating inventory
"""
form = cgi.FieldStorage()
liuser = form.getfirst("username")
mygiantlist = []
listcopy = []

"""
1. Goes through the inventory file
2. If the item is checked off on the catalogue page
	- Check if the number requested is less than the stock
		- If the number is smaller, add the item, # requested, and unit price to both lists
	- If the # requested is larger, add the item, max stock, and unit price to both lists
3. If the item is not checked off, just add it to the list for inventory update
"""
with open('../data/Inventory.csv', 'rt') as cofile:
	colist = cofile.read()
cofile.closed
splitlist = colist.split("\n")
splitlist.pop()
splitlist.reverse()

while len(splitlist) > 0:
	nline = splitlist.pop()
	p = nline.split(",")
	checkme = form.getfirst(str(p[0]))
	if checkme == "true":
		pupnum = str(p[0]) + 'num'
		numtoget = form.getfirst(pupnum)
		if int(p[1]) >= int(numtoget):
			mygiantlist.append(str(p[0]))
			mygiantlist.append(numtoget)
			mygiantlist.append(int(p[2]))
			listcopy.append(str(p[0]))
			newstock = int(p[1]) - int(numtoget)
			listcopy.append(newstock)
			listcopy.append(int(p[2]))
			listcopy.append(str(p[3]))
		else:
			mygiantlist.append(str(p[0]))
			mygiantlist.append(p[1])
			mygiantlist.append(int(p[2]))
			listcopy.append(str(p[0]))
			listcopy.append(0)
			listcopy.append(int(p[2]))
			listcopy.append(str(p[3]))
	else:
		listcopy.append(str(p[0]))
		if int(p[1]) == 0:
			listcopy.append(randomRestock())
		else:
			listcopy.append(int(p[1]))
		listcopy.append(int(p[2]))
		listcopy.append(str(p[3]))

"""
Since lists are LIFO in python, reversing the list makes it easier to deal with
"""
mygiantlist.reverse()
listcopy.reverse()

"""
1. If the hidden field is not empty, user might be logged in
	- If the username is in the loggedin file generate the bill and update inventory
	- If the username is not in the loggedin file generate the error page
2. If the hidden field is empty, user is not logged in
	- Generate error page
"""
if liuser != "null":
	isLogged = False
	thisline = []
	with open('../data/LoggedIn.csv', 'rt') as fline:
		thisline = fline.read()
	fline.closed
	mlist = thisline.split("\n")
	for bits in mlist:
		if liuser == bits:
			isLogged = True
	if isLogged:
		generateBill(liuser, mygiantlist)
		removeInventory(listcopy)
	else:
		generateError()
else:
	generateError()





