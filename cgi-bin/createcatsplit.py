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
	alllist = []
	retlist = []
	with open('data/Inventory.csv', 'rt') as allfile:
		alllist = allfile.read()
	allfile.closed
	hitlist = alllist.split("\n")
	hitlist.pop()
	hitlist.reverse()

	return hitlist

'''
This method returns the HTML necessary to generate four items in a row
@param olist The description list
@param fpos The first item in the row
@param tpos The second item in the row
@param thpos The third item in the row
@param fopos The fourth item in the row
@return The HTML needed to render a row of 4 items
'''
def getFour(fpos, tpos, thpos, fopos):
	fime = """
	<tr>
		<td><img src = "images/""" + fpos[0] + """.jpg" width="200" height="200"> </img></td>
		<td><img src = "images/""" + tpos[0] + """.jpg" width="200" height="200"> </img></td>
		<td><img src = "images/""" + thpos[0] + """.jpg" width="200" height="200"> </img></td>
		<td><img src = "images/""" + fopos[0] + """.jpg" width="200" height="200"> </img></td>
	</tr>
	<tr>
		<td class="breed">""" + fpos[0] + """</td>
		<td class="breed">""" + tpos[0] + """</td>
		<td class="breed">""" + thpos[0] + """</td>
		<td class="breed">""" + fopos[0] + """</td>
	</tr>
	<tr>
		<td>""" + str(fpos[3]) + """</td>
		<td>""" + str(tpos[3]) + """</td>
		<td>""" + str(thpos[3]) + """</td>
		<td>""" + str(fopos[3]) + """</td>
	</tr>
	<tr>
		<td>Number in stock:  """ + fpos[1] + """</td>
		<td>Number in stock:  """ + tpos[1] + """</td>
		<td>Number in stock:  """ + thpos[1] + """</td>
		<td>Number in stock:  """ + fopos[1] + """</td>
	</tr>
	<tr>
		<td><input name = \"""" + fpos[0] + """\" type = "checkbox" value = "true"></input>
			<input class="catalogue" name = \"""" + fpos[0] + """num" type = "text" value = "0"></input>
		</td>
		<td><input name = \"""" + tpos[0] + """\" type = "checkbox" value = "true"></input>
			<input class="catalogue" name = \"""" + tpos[0] + """num" type = "text" value = "0"></input>
		</td>
		<td><input name = \"""" + thpos[0] + """\" type = "checkbox" value = "true"></input>
			<input class="catalogue" name = \"""" + thpos[0] + """num" type = "text" value = "0"></input>
		</td>
		<td><input name = \"""" + fopos[0] + """\" type = "checkbox" value = "true"></input>
			<input class="catalogue" name = \"""" + fopos[0] + """num" type = "text" value = "0"></input>
		</td>
	</tr>
	"""

	return fime

'''
This method returns the HTML necessary to generate three items in a row
@param olist The description list
@param fpos The first item in the row
@param tpos The second item in the row
@param thpos The third item in the row
@return The HTML needed to render a row of 3 items
'''
def getThree(fpos, tpos, thpos):
	fime = """
	<tr>
		<td><img src = "images/""" + str(fpos[0]) + """.jpg" width="200" height="200"> </img></td>
		<td><img src = "images/""" + str(tpos[0]) + """.jpg" width="200" height="200"> </img></td>
		<td><img src = "images/""" + str(thpos[0]) + """.jpg" width="200" height="200"> </img></td>
	</tr>
	<tr>
		<td class="breed">""" + str(fpos[0]) + """</td>
		<td class="breed">""" + str(tpos[0]) + """</td>
		<td class="breed">""" + str(thpos[0]) + """</td>
	</tr>
	<tr>
		<td>""" + str(fpos[3]) + """</td>
		<td>""" + str(tpos[3]) + """</td>
		<td>""" + str(thpos[3]) + """</td>
	</tr>
	<tr>
		<td>Number in stock:  """ + str(fpos[1]) + """</td>
		<td>Number in stock:  """ + str(tpos[1]) + """</td>
		<td>Number in stock:  """ + str(thpos[1]) + """</td>
	</tr>
		<tr>
		<td><input name = \"""" + fpos[0] + """\" type = "checkbox" value = "true"></input>
			<input class="catalogue" name = \"""" + fpos[0] + """num" type = "text" value = "0"></input>
		</td>
		<td><input name = \"""" + tpos[0] + """\" type = "checkbox" value = "true"></input>
			<input class="catalogue" name = \"""" + tpos[0] + """num" type = "text" value = "0"></input>
		</td>
		<td><input name = \"""" + thpos[0] + """\" type = "checkbox" value = "true"></input>
			<input class="catalogue" name = \"""" + thpos[0] + """num" type = "text" value = "0"></input>
		</td>
	</tr>"""
	return fime

'''
This method returns the HTML necessary to generate two items in a row
@param olist The description list
@param fpos The first item in the row
@param tpos The second item in the row
@return The HTML needed to render a row of 2 items
'''
def getTwo(fpos, tpos):
	fime = """
	<tr>
		<td><img src = "images/""" + str(fpos[0]) + """.jpg" width="200" height="200"> </img></td>
		<td><img src = "images/""" + str(tpos[0]) + """.jpg" width="200" height="200"> </img></td>
	</tr>
	<tr>
		<td class="breed">""" + str(fpos[0]) + """</td>
		<td class="breed">""" + str(tpos[0]) + """</td>
	</tr>
	<tr>
		<td>""" + str(fpos[3]) + """</td>
		<td>""" + str(tpos[3]) + """</td>
	</tr>
	<tr>
		<td>Number in stock:  """ + str(fpos[1]) + """</td>
		<td>Number in stock:  """ + str(tpos[1]) + """</td>
	</tr>
	<tr>
		<td><input name = \"""" + fpos[0] + """\" type = "checkbox" value = "true"></input>
			<input class="catalogue" name = \"""" + fpos[0] + """num" type = "text" value = "0"></input>
		</td>
		<td><input name = \"""" + tpos[0] + """\" type = "checkbox" value = "true"></input>
			<input class="catalogue" name = \"""" + tpos[0] + """num" type = "text" value = "0"></input>
		</td>
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
		<td><img src = "images/""" + str(fpos[0]) + """.jpg" width="200" height="200"> </img></td>
	</tr>
	<tr>
		<td>""" + str(fpos[0]) + """</td>
	</tr>
	<tr>
		<td>""" + str(fpos[3]) + """</td>
	</tr>
	<tr>
		<td>Number in stock:  """ + str(fpos[1]) + """</td>
	</tr>
	<tr>
		<td><input name = \"""" + fpos[0] + """\" type = "checkbox" value = "true"></input>
			<input class="catalogue" name = \"""" + fpos[0] + """num" type = "text" value = "0"></input>
		</td>
	</tr>"""
	return fime


'''
This method generates the HTML to be rendered for the catalogue from the current inventory.
@param ulist The list that contains the name of all inventory items
@param dlist The list that contains the description of all inventory items
@param name The username
'''	
def genCat(urlist):

	fwr = open('catalogue.html', 'wt')
	
	mewssage = """<!doctype html>
	<html>
	<head>
	<link rel="stylesheet" type="text/css" href="stylesheets/main.css">
	<title>catalogue</title>
	<style type="text/css"></style>
	</head>
	<div id="home">
	<div id="yellow">
	<div id="catalogue">
	<center>
	<h1>Catalogue</h1>
	<form name="submit" method="post" action="cgi-bin/Purchase.py">
	<input name = "username" type = "hidden" value =\"""" + str(sys.argv[1]) + """\"></input>
	<table>"""
	fwr.write(mewssage)

	while len(urlist) > 0:
		if len(urlist) >= 4:
			fwr.write(getFour(urlist.pop().split(","), urlist.pop().split(","), urlist.pop().split(","), urlist.pop().split(",")))
		elif len(urlist) == 3:
			fwr.write(getThree(urlist.pop().split(","), urlist.pop().split(","), urlist.pop().split(",")))
		elif len(urlist) == 2:
			fwr.write(getTwo(urlist.pop().split(","), urlist.pop().split(",")))
		else:
			fwr.write(getOne(urlist.pop().split(",")))

	mewssage = """
	</table>
	<input class = "bufferbutton" name="submit" type="submit" value="buy me"></input>
	</form>"""
	fwr.write(mewssage)

	if str(sys.argv[1]) != "null":
		fwr.write("""
		<form name="logout" method="post" action="b.cgi">
		<input name = "username" type = "hidden" value =\"""" + str(sys.argv[1]) + """\"></input>
		<input class = "bufferbutton" type="submit" value="Log out"></input>
		</form>""")

	fwr.write("""
	</center>
	</div>
	</div>
	</div>
	</body>
	</html>""")

	fwr.close()


'''
Get the inventory and description lists
Since lists are LIFO, reverse them
'''
thislist = getAllInv()

genCat(thislist)



















