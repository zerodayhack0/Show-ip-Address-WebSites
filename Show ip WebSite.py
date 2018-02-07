import socket

name_site = raw_input("Enter Address Web Site : ")

print(socket.gethostbyname(name_site))