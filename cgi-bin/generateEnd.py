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
<form name="goback2home" method="post" action="../index.html">
<input name = "username" type = "hidden" value =\"""" + str(liuser) + """\"></input>
<p><input type = "submit" value = "home"></input></p>
</form>
<form name="goback2catalogue" method="post" action="../c.cgi">
<input name = "username" type = "hidden" value =\"""" + str(liuser) + """\"></input>
<p><input type = "submit" value = "catalogue"></input></p>
</form>
<form name="goback" method="post" action="../b.cgi">
<input name = "username" type = "hidden" value =\"""" + str(liuser) + """\"></input>
<p><input type = "submit" value = "log out"></input></p>
</form>
</center>
</div>
</body>
</html>"""
