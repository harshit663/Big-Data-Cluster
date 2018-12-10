#!/usr/bin/python36

print("Content-type: text/html")
print("\n")

print("""
<center>
<h1>Welcome to hadoop cluster Manager</h1>
What do want you to do?<br><br>
<a href='hadoop_list.py'>Check Hadoop hdfs filesystem</a><br><br>
<a href=''>Create a directory in hdfs filesystem</a><br>
<form action='hadoop_create.py'>
<input type='text' name='fname' placeholder='Directory Name'/><input type='submit' value='Create' />
</form>
<a href=''>Upload a file to hdfs filesystem</a><br><br>
<a href='http://192.168.43.211:50070'>Check the cluster</a><br><br>
<a href='hadoop.py' target='cframe'>Do things Manually</a><br><br>
<iframe name='cframe' width='100%' height='50%'></iframe>
</center> 
""")


