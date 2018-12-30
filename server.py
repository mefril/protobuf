#!/usr/bin/env python3
import sys
sys.path.insert(0, './proto_py')

import messages_pb2
import socket


mes = messages_pb2.Message();

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	conn, addr = s.accept()
	with conn:
		print('Connected by', addr)
		while True:
			data = conn.recv(1024)
			if not data:
				break
			mes.ParseFromString(data)
			mes.name = 'changed on a server'
			mes.id = 24234
			print('end')
			conn.sendall(mes.SerializeToString())