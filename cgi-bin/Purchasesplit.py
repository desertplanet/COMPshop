#!/usr/bin/env python
# -*- coding: UTF-8 -*-

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
	<p>To return to the catalogue, click <a href = ../catalogue.html>here</a>.</p>
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
	<h3><a href = ../thankyou.html>CHECKOUT</a></h3>
	<p><a href = ../index.html>HOME</a></p>
	<p><a href = ../catalogue.html>CATALOGUE</a></p>
	</body>
	</html>"""

"""
This method overwrites the inventory based on the list that contains the entire new inventory.
@param lcpy The list that contains the name, new stock amount, and price of all items.
"""
def removeInventory(lcpy):
	with open('../data/Inventory.csv', 'wt') as refile:
		rewriter = csv.writer(refile, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
		while len(lcpy) > 0:
			uname = lcpy.pop()
			ustock = lcpy.pop()
			uprice = lcpy.pop()
			rewriter.writerow([uname,ustock,uprice])
"""
This method gets the price of the item from the inventory
@param pupname The name of the item
@return Returns the price of the item
"""
def getPrice(pupname):
	f = open('../data/Inventory.csv', 'rt')
	price = 0
	for line in f:
		mlist = line.split(',')
		if pupname = str(mlist[0]):
			price = int9mlist[2])
	f.close()
	return price


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
if liuser != "":
	isLogged = False
	f = open('../data/LoggedIn.csv', 'rt')
	for fline in f:
		flist = fline.split('\n')
		if liuser == str(flist[0]):
			isLogged = True
	if isLogged:
		generateBill(liuser, mygiantlist)
		removeInventory(listcopy)
	else:
		generateError()
else:
	generateError()





