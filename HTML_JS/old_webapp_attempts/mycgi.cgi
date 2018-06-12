#!/usr/bin/env python

import cgitb, cgi
sys.path.insert(0,'networkxwork.py')
import networkxwork as path
form = cgi.FieldStorage()
cgitb.enable()
#path.getPath("Amarr", "Jita")
print ("Content-Type: text/plain;charset=utf-8")
print
print ("Hello World!")
