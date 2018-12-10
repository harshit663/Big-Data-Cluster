#!/usr/bin/python36

import subprocess as sp

print("Content-type: text/html")

o = sp.getstatusoutput("sudo ansible-playbook hadoop.yml")

if o[0] == 0:
	print("location: hadoop2.py")
	print()

else:
	print()
	print(0[1])

