#!/usr/bin/python36

import subprocess as sp

print("Content-type: text/html")
print("\n")

#s_out = sp.getstatusoutput("sudo hadoop fs -ls)
print("""
<center>
<h1>Welcome to Hadoop hdfs filesystem</h1>
<a href='hadoop_manager.py'>Go back to cluster Manager</a>
</center>
""")
