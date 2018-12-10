#!/usr/bin/python36

import subprocess as sp
import cgi

print("Content-type: text/html")

form = cgi.FieldStorage()
fname = form.getvalue('fname')

#s_out = sp.getstatusoutput("sudo hadoop fs -mkdir /{}".format(fname))
if s_out[0] == 0:
	print("location: hadoop_manager.py")
	print("\n")
else:
	print("\n")
	print(s[1])
