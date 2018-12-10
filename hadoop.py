#!/usr/bin/python36

import subprocess as sp

print("Content-type: text/html")
print("\n")

n_out = sp.getoutput("sudo nmap 192.168.43.0/24")
n_out = n_out.split('\n\n')

print("""
<center>
<h1>Welcome to Hadoop Setup</h1>
<form action='hadoop2.py'>
""")

for i in n_out:
	if "Unknown" in i:
		pass
	else:
		try:
			x = i.index('192')
			ip_out = i[x:x+14].replace(')', '').rstrip()
			print("<input type='radio' name='ip' value='{}' >".format(ip_out))
			print(ip_out)
			print("<br><br>")
		except:
			print("Select an ip to make Master node ")
			print("<br><br>")
		
print("""
<input type='submit'/>   <input type='reset'/></form>
</center>
""")





