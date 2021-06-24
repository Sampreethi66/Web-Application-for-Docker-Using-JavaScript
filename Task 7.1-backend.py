#!/usr/bin/python3

import cgi
import subprocess
import time

print("content-typwe.text/html")
print()
f=cgi.FieldStorage()
cmd=f.getvalue("X")
print("<h2>Your Command is :-</h2>",cmd,"<h2>\n OutPut is:-</h2>")
output=subprocess.getoutput("sudo"+cmd)
print("*"*100)
print()
print(output)
print()
print("*"*100)
time.sleep(3)
print("<h1> thank you for usig this Docker UI Pahe</h1>")
