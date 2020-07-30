#import os
#import socket
#import sys
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Create a TCP/IP socket
#server_ip = input('Enter server IP : ')
#rep = os.system('ping ' + server_ip)
#print(" ")
#print(" ")
#print(" ")
#if rep == 0:
#    print ("------:server is up:-------")
#else:
#    print ("------:server is down:------")


import sys
import os
import platform
import subprocess

plat = platform.system()
scriptDir = sys.path[0]
hosts = os.path.join(scriptDir, 'hosts.txt')
hostsFile = open(hosts, "r")
lines = hostsFile.readlines()
if plat == "Windows":
    for line in lines:
        line = line.strip( )
        ping = subprocess.Popen(["ping", "-n", "1", "-l", "1", "-w", "100", line],
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
        )
        out, error = ping.communicate()
        print (out)
        print (error)

if plat == "Linux":
    for line in lines:
        line = line.strip( )
        ping = subprocess.Popen(["ping", "-c", "1", "-l", "1", "-s", "1", "-W", "1", line],
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
        )
        out, error = ping.communicate()
        print (out)
        print (error)

hostsFile.close()
