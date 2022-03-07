#!/usr/bin/env python3
from email.mime import image
import socket
import sys, getopt

def main(argv):

   try:
      opts, args = getopt.getopt(argv,"Hh:p:",["host=","port="])
   except getopt.GetoptError:
      print ('yacurl.py -h <host> -p <port>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-H':
         print ('yacurl.py -h <host> -p <port>')
         sys.exit()
      elif opt in ("-h", "--host"):
         host = str(arg)
      elif opt in ("-p", "--port"):
         port = int(arg)
   return host,port

if __name__ == "__main__":
    host,port=main(sys.argv[1:])
    response = ""
    host = host.replace("http://","")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        request = f"GET / HTTP/1.1\r\nHost: {host}:{port}\r\n\r\n".encode()
      
        s.sendall(request)
        while True:
         recv = s.recv(1024)
         if recv == b'':
               break
         response += recv.decode()
      
        if response.split('\r\n\r\n',1)[1]:
          with open("index.html", "w") as f:
           f.write(response.split('\r\n\r\n',1)[1])
           f.close()
   
      

        print(response)
      
