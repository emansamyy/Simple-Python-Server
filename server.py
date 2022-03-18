# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 14:36:31 2022

@author: User
"""

import socket
SRV_ADDR = input("enter the server's IP address")
SRV_PORT = input("enter the server's port")

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


s.bind(SRV_ADDR,SRV_PORT)
s.listen(1)
 #or instead of bind and listen:
     
  #  s.connect(SRV_ADDR,SRV_PORT)

print("server started waiting for connections")
connection,address = s.accept()
print("client connected with adddress" ,address)

while 1:
    data = connection.recv(1024)
    if not data:
        break
    connection.sendall("Message received")
    print(data.decode('utf-8'))
connection.close()