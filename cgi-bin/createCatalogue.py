#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import csv


def genImageRow(imglst):
	return

def genDescripRow(deslst):
	return

def genCheckRow(checklst):
	return

def genFieldRow(fieldlst):
	return

def genCat():
	f = open('helloworld.html','w')

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
	<form name="submit" method="post" action="cgi-bin/Purchase.py">"""

	f.write(message)
	f.close()

	g = open('helloworld.html', 'a')

	message = '''<input name = "username" type = "hidden" value ="''' + str(sys.argv[1]) + '''"></input>'''
	g.write(message)
	
	message = """<table>"""
	g.write(message)

	with open('../data/Inventory.csv', 'wt') as cfile:
		creader = csv.reader(cfile, delimiter=',', quotechar=' ')
		count = 0
		crelist = []
		for epup in creader:
			if count < 4:
				crelist.append(epup[0])
				count = count + 1
			else:
				crelist.reverse()
				fpos = crelist.pop()
				tpos = crelist.pop()
				thpos= crelist.pop()
				fopos = crelist.pop()
				message = '''
				<tr>
					<td><img src = "images/''' + str(fpos) + '''.jpg" width="200" height="200"> </img></td>
					<td><img src = "images/''' + str(tpos) + '''.jpg" width="200" height="200"> </img></td>
					<td><img src = "images/''' + str(thpos) + '''.jpg" width="200" height="200"> </img></td>
					<td><img src = "images/''' + str(fopos) + '''.jpg" width="200" height="200"> </img></td>
				</tr>
				<tr>
					<td>''' + str(fpos) + '''</td>
					<td>''' + str(tpos) + '''</td>
					<td>''' + str(thpos) + '''</td>
					<td>''' + str(fopos) + '''</td>
				</tr>
				<tr>
					<td><input name = "''' + str(fpos) + '''" type = "checkbox" value = "true"></input></td>
					<td><input name = "''' + str(tpos) + '''" type = "checkbox" value = "true"></input></td>
					<td><input name = "''' + str(thpos) + '''" type = "checkbox" value = "true"></input></td>
					<td><input name = "''' + str(fopos) + '''" type = "checkbox" value = "true"></input></td>
				</tr>
				<tr>
					<td><input name = "''' + str(fpos) + '''num" type = "text" value = "0"></input></td>
					<td><input name = "''' + str(tpos) + '''num" type = "text" value = "0"></input></td>
					<td><input name = "''' + str(thpos) + '''num" type = "text" value = "0"></input></td>
					<td><input name = "''' + str(fopos) + '''num" type = "text" value = "0"></input></td>
				</tr>'''
				g.write(message)
				count = 0
	message = '''</table>
	<input name="submit" type="submit" value="buy me"></input>
	</form>
	</body>
	</html>'''

	g.write(message)
	g.close()



print "Content-Type: text/html;charset=utf-8"
print
print "hi"
























