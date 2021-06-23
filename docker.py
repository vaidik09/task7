#!/usr/bin/python3

import cgi
import subprocess
import time

print("content-type: text/html")
print()
f = cgi.FieldStorage()
cmd = f.getvalue("x")

if cmd == "list":
    cmd = "docker ps"
    o = subprocess.getoutput("sudo " + cmd)
elif cmd == "images":
    cmd = "docker images"
    o = subprocess.getoutput("sudo " + cmd)
elif cmd == "run":
    cmd = "docker run -dit " + f.getvalue("y") + ":" + f.getvalue("z")
    o = subprocess.getoutput("sudo " + cmd)
elif cmd == "exec":
    cmd = "docker stop " + f.getvalue("y")
    o = subprocess.getoutput("sudo " + cmd)
elif cmd == "exec1":
    cmd = "docker start " + f.getvalue("y")
    o = subprocess.getoutput("sudo " + cmd)
elif cmd == "rem":
    cmd = "sudo docker rm " + f.getvalue("y") + " --force"
    o = subprocess.getoutput("sudo " + cmd)
elif cmd == "remi":
    cmd = "docker rmi " + f.getvalue("y") + " --force"
    o = subprocess.getoutput("sudo " + cmd)


print(cmd + "<br />")
print("<br />")
print("<pre>")
print(o)
print("</pre>")
print("<br />")
