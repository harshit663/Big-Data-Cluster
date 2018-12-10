#!/usr/bin/python36

import subprocess as sp

print("Content-type: text/html")

s = sp.getstatusoutput("sudo ansible-playbook /media/sf_share/ansible/hadoop/slave.yml")
if s[0] == 0:
	print()
	print("location: hadoop_manager.py")

else:
	print(s[1])

