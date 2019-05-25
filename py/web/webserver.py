# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 22:46:58 2019

@author: zhengjt
"""

import socket
 
HOST, PORT = '', 8888
 
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print('Serving HTTP on port %s ...' % PORT)
while True:
    print('1')
    client_connection, client_address = listen_socket.accept()
    print('1.5')
    request = client_connection.recv(1024)
    print('2')
    print(request)
 
    http_response = """
HTTP/1.1 200 OK
 
Hello, World!
"""
    http_response_data = http_response.encode(encoding='utf_8')
    print('3')
    client_connection.sendall(http_response_data)
    client_connection.close()