#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import csv
import cgi

'''
This method returns a list of the entire inventory, regardless of whether or not
it is out of stock.
@return A list with all the names of the inventory
'''
def getAllInv():
	with open('data/Inventory.csv', 'rt') as cfile:
		creader = csv.reader(cfile, delimiter=',', quotechar=' ')
		crelist = []
		for epup in creader:
			crelist.append(epup[0])
	return crelist
'''
This method returns a list of all the descriptions.
@return A list with all the descriptions of everything in the inventory
'''
def getDescripList():
	with open('data/Descriptions.csv', 'rt') as cfile:
		creader = csv.reader(cfile, delimiter=',', quotechar=' ')
		crelist = []
		for epup in creader:
			crelist.append(epup[1])
	return crelist
'''
This method gets the amount of stock for the item
@param pupname The item to get the amount of stock for
@return The amount of stock
'''
def getStock(pupname):
	with open('data/Inventory.csv', 'rt') as cfile:
		creader = csv.reader(cfile, delimiter=',', quotechar=' ')
		for epup in creader:
			if str(epup[0]) == pupname:
				return str(epup[1])
	
'''
This method returns the HTML necessary to generate four items in a row
@param olist The description list
@param fpos The first item in the row
@param tpos The second item in the row
@param thpos The third item in the row
@param fopos The fourth item in the row
@return The HTML needed to render a row of 4 items
'''
def getFour(olist, fpos, tpos, thpos, fopos):
	fime = """
	<tr>
		<td><img src = "images/""" + str(fpos) + """.jpg" width="200" height="200"> </img></td>
		<td><img src = "images/""" + str(tpos) + """.jpg" width="200" height="200"> </img></td>
		<td><img src = "images/""" + str(thpos) + """.jpg" width="200" height="200"> </img></td>
		<td><img src = "images/""" + str(fopos) + """.jpg" width="200" height="200"> </img></td>
	</tr>
	<tr>
		<td>""" + str(fpos) + """</td>
		<td>""" + str(tpos) + """</td>
		<td>""" + str(thpos) + """</td>
		<td>""" + str(fopos) + """</td>
	</tr>
	<tr>
		<td>""" + olist.pop() + """</td>
		<td>""" + olist.pop() + """</td>
		<td>""" + olist.pop() + """</td>
		<td>""" + olist.pop() + """</td>
	</tr>
	<tr>
		<td>Number in stock:  """ + getStock(fpos) + """</td>
		<td>Number in stock:  """ + getStock(tpos) + """</td>
		<td>Number in stock:  """ + getStock(thpos) + """</td>
		<td>Number in stock:  """ + getStock(fopos) + """</td>
	</tr>
	<tr>
		<td><input name = \"""" + str(fpos) + """\" type = "checkbox" value = "true"></input></td>
		<td><input name = \"""" + str(tpos) + """\" type = "checkbox" value = "true"></input></td>
		<td><input name = \"""" + str(thpos) + """\" type = "checkbox" value = "true"></input></td>
		<td><input name = \"""" + str(fopos) + """\" type = "checkbox" value = "true"></input></td>
	</tr>
	<tr>
		<td><input name = \"""" + str(fpos) + """num" type = "text" value = "0"></input></td>
		<td><input name = \"""" + str(tpos) + """num" type = "text" value = "0"></input></td>
		<td><input name = \"""" + str(thpos) + """num" type = "text" value = "0"></input></td>
		<td><input name = \"""" + str(fopos) + """num" type = "text" value = "0"></input></td>
	</tr>"""
	return fime

'''
This method returns the HTML necessary to generate three items in a row
@param olist The description list
@param fpos The first item in the row
@param tpos The second item in the row
@param thpos The third item in the row
@return The HTML needed to render a row of 3 items
'''
def getThree(olist, fpos, tpos, thpos):
	fime = """
	<tr>
		<td><img src = "images/""" + str(fpos) + """.jpg" width="200" height="200"> </img></td>
		<td><img src = "images/""" + str(tpos) + """.jpg" width="200" height="200"> </img></td>
		<td><img src = "images/""" + str(thpos) + """.jpg" width="200" height="200"> </img></td>
	</tr>
	<tr>
		<td>""" + str(fpos) + """</td>
		<td>""" + str(tpos) + """</td>
		<td>""" + str(thpos) + """</td>
	</tr>
	<tr>
		<td>""" + olist.pop() + """</td>
		<td>""" + olist.pop() + """</td>
		<td>""" + olist.pop() + """</td>
	</tr>
	<tr>
		<td>Number in stock:  """ + getStock(fpos) + """</td>
		<td>Number in stock:  """ + getStock(tpos) + """</td>
		<td>Number in stock:  """ + getStock(thpos) + """</td>
	</tr>
	<tr>
		<td><input name = \"""" + str(fpos) + """\" type = "checkbox" value = "true"></input></td>
		<td><input name = \"""" + str(tpos) + """\" type = "checkbox" value = "true"></input></td>
		<td><input name = \"""" + str(thpos) + """\" type = "checkbox" value = "true"></input></td>
	</tr>
	<tr>
		<td><input name = \"""" + str(fpos) + """num" type = "text" value = "0"></input></td>
		<td><input name = \"""" + str(tpos) + """num" type = "text" value = "0"></input></td>
		<td><input name = \"""" + str(thpos) + """num" type = "text" value = "0"></input></td>
	</tr>"""
	return fime

'''
This method returns the HTML necessary to generate two items in a row
@param olist The description list
@param fpos The first item in the row
@param tpos The second item in the row
@return The HTML needed to render a row of 2 items
'''
def getTwo(olist, fpos, tpos):
	fime = """
	<tr>
		<td><img src = "images/""" + str(fpos) + """.jpg" width="200" height="200"> </img></td>
		<td><img src = "images/""" + str(tpos) + """.jpg" width="200" height="200"> </img></td>
	</tr>
	<tr>
		<td>""" + str(fpos) + """</td>
		<td>""" + str(tpos) + """</td>
	</tr>
	<tr>
		<td>""" + olist.pop() + """</td>
		<td>""" + olist.pop() + """</td>
	</tr>
	<tr>
		<td>Number in stock:  """ + getStock(fpos) + """</td>
		<td>Number in stock:  """ + getStock(tpos) + """</td>
	</tr>
	<tr>
		<td><input name = \"""" + str(fpos) + """\" type = "checkbox" value = "true"></input></td>
		<td><input name = \"""" + str(tpos) + """\" type = "checkbox" value = "true"></input></td>
	</tr>
	<tr>
		<td><input name = \"""" + str(fpos) + """num" type = "text" value = "0"></input></td>
		<td><input name = \"""" + str(tpos) + """num" type = "text" value = "0"></input></td>
	</tr>"""
	return fime

'''
This method returns the HTML necessary to generate one item in a row
@param olist The description list
@param fpos The first item in the row
@return The HTML needed to render a row of 1 item
'''
def getOne(olist, fpos):
	fime = """
	<tr>
		<td><img src = "images/""" + str(fpos) + """.jpg" width="200" height="200"> </img></td>
	</tr>
	<tr>
		<td>""" + str(fpos) + """</td>
	</tr>
	<tr>
		<td>""" + olist.pop() + """</td>
	</tr>
	<tr>
		<td>Number in stock:  """ + getStock(fpos) + """</td>
	</tr>
	<tr>
		<td><input name = \"""" + str(fpos) + """\" type = "checkbox" value = "true"></input></td>
	</tr>
	<tr>
		<td><input name = \"""" + str(fpos) + """num" type = "text" value = "0"></input></td>
	</tr>"""
	return fime


'''
This method generates the HTML to be rendered for the catalogue from the current inventory.
@param ulist The list that contains the name of all inventory items
@param dlist The list that contains the description of all inventory items
@param name The username
'''	
def genCat(ulist, dlist):
	f = open('catalogue.html', 'wt')
	
	message = """<!doctype html>
	<html>
	<head>
	<link rel="stylesheet" type="text/css" href="stylesheets/main.css">
	<title>catalogue</title>
	<style type="text/css"></style>
	</head>
	<div id="home">
	<center>
	<h1>Catalogue</h1>
	<form name="submit" method="post" action="cgi-bin/Purchase.py">
	<input name = "username" type = "hidden" value =\"""" + str(sys.argv[1]) + """\"></input>
	<table>"""
	f.write(message)

	while len(ulist) > 0:
		if len(ulist) >= 4:
			message = getFour(dlist, ulist.pop(), ulist.pop(), ulist.pop(), ulist.pop())
		elif len(ulist) == 3:
			message = getThree(dlist, ulist.pop(), ulist.pop(), ulist.pop())
		elif len(ulist) == 2:
			message = getTwo(dlist, ulist.pop(), ulist.pop())
		else:
			message = getOne(dlist, ulist.pop())
			
		f.write(message)

	message = """
	</table>
	<input name="submit" type="submit" value="buy me"></input>
	</form>
	<form name="logout" method="post" action="b.cgi">
	<input name = "username" type = "hidden" value =\"""" + str(sys.argv[1]) + """\"></input>
	<input name="logout" type="submit" value="Log out"></input>
	</form>
	</center>
	</div>
	</body>
	</html>"""

	f.write(message)
	f.close()


'''
Get the inventory and description lists
Since lists are LIFO, reverse them
'''
thislist = getAllInv()
descriplist = getDescripList()
thislist.reverse()
descriplist.reverse()

genCat(thislist, descriplist)



















