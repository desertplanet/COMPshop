#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import csv


def getAllInv():
	with open('data/Inventory.csv', 'rt') as cfile:
		creader = csv.reader(cfile, delimiter=',', quotechar=' ')
		crelist = []
		for epup in creader:
			crelist.append(epup[0])
	return crelist

def getStock(pupname):
	with open('data/Inventory.csv', 'rt') as cfile:
		creader = csv.reader(cfile, delimiter=',', quotechar=' ')
		for epup in creader:
			if str(epup[0]) == pupname:
				return str(epup[1])

def getFour(fpos, tpos, thpos, fopos):
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

def getThree(fpos, tpos, thpos):
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

def getTwo(fpos, tpos):
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
		<td><input name = \"""" + str(fpos) + """\" type = "checkbox" value = "true"></input></td>
		<td><input name = \"""" + str(tpos) + """\" type = "checkbox" value = "true"></input></td>
	</tr>
	<tr>
		<td><input name = \"""" + str(fpos) + """num" type = "text" value = "0"></input></td>
		<td><input name = \"""" + str(tpos) + """num" type = "text" value = "0"></input></td>
	</tr>"""
	return fime

def getOne(fpos):
	fime = """
	<tr>
		<td><img src = "images/""" + str(fpos) + """.jpg" width="200" height="200"> </img></td>
	</tr>
	<tr>
		<td>""" + str(fpos) + """</td>
	</tr>
	<tr>
		<td><input name = \"""" + str(fpos) + """\" type = "checkbox" value = "true"></input></td>
	</tr>
	<tr>
		<td><input name = \"""" + str(fpos) + """num" type = "text" value = "0"></input></td>
	</tr>"""
	return fime
	
def genCat(ulist):
	f = open('catalogue.html','w')

	message = """<!doctype html>
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
	<h1>Catalogue</h1>
	<form name="submit" method="post" action="cgi-bin/Purchase.py">
	<input name = "username" type = "hidden" value =\"""" + str(sys.argv[1]) + """\"></input>
	<table>"""

	f.write(message)

	while len(ulist) > 0:
		if len(ulist) >= 4:
			message = getFour(ulist.pop(), ulist.pop(), ulist.pop(), ulist.pop())
		elif len(ulist) == 3:
			message = getThree(ulist.pop(), ulist.pop(), ulist.pop())
		elif len(ulist) == 2:
			message = getTwo(ulist.pop(), ulist.pop())
		else:
			message = getOne(ulist.pop())
			
		f.write(message)

	message = """
	</table>
	<input name="submit" type="submit" value="buy me"></input>
	</form>
	</body>
	</html>"""

	f.write(message)
	f.close()



print "Content-Type: text/html;charset=utf-8"
print

thislist = getAllInv()
thislist.reverse()
genCat(thislist)

print "I worked"



















