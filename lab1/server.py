#!/usr/bin/env python3

import socket
import sys, getopt

def main(argv):

   try:
      opts, args = getopt.getopt(argv,"H:p:",["port="])
   except getopt.GetoptError:
      print ('yacurl.py -p <port>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-H':
         print ('yacurl.py -p <port>')
         sys.exit()
      elif opt in ("-p", "--port"):
         port = int(arg)
   return port

HOST = '0.0.0.0'  # Standard loopback interface address (localhost)

if __name__ == "__main__":
    port=main(sys.argv[1:])
    print("listening by port = ",port)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        port=main(sys.argv[1:])
        s.bind((HOST, port))
        s.listen(1)

        response =  b"HTTP/1.1 200 OK\n\nHello World"
        while True:
         try:
               conn, addr = s.accept()
               req = conn.recv(1024).decode()
               print(req)
               conn.sendall(response)
               conn.close()
         except Exception as E:
               print(E)