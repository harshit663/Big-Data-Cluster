#!/usr/bin/python36

import subprocess as sp

print("content-type: /text/html")


s = sp.getstatusoutput("sudo ansible-playbook /media/sf_share/ansible/hadoop/master.yml")
if s[0] == 0:
	print("location: hadoop3.py")
	print("\n")

else:
	print("\n")
	print(s[1])


