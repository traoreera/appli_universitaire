import socket
import sys

try:
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("succes ...")
except socket.error:
    print("socket error")
port = 80
try:
    host_ip = socket.gethostbyname('www.github.com')
    print(f"host ip : {host_ip}")
except socket.gaierror:
    print("error resolving host")
    sys.exit()
s.connect((host_ip,port))
print(f"socket as succsfully connected github port: {host_ip}")