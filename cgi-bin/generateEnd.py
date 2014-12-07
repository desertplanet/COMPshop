#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
liuser = form.getfirst("username")

print "Content-Type: text/html;charset=utf-8"
print
print """
<!doctype html>
<html>
<head>
<link rel="stylesheet" type="text/css" href="../stylesheets/main.css">
<title>catalogue</title>
<style type="text/css"></style>
</head>
<body style="color:black; font-family:helvetica;">
<div id="home">
<center>
<h3>Thank you for your purchase!</h3>
<p>You can return to the home page by clicking <a href = ../index.html>here</a>.</p>
<form name="goback" method="post" action="../c.cgi">
<input name = "username" type = "hidden" value =\"""" + str(liuser) + """\"></input>
<p>To return to the catalogue, click <input type = "submit" value = "here"></input>.</p>
</form>
</center>
</div>
</body>
</html>"""
