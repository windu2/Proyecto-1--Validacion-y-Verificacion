import socket
import codecs
import logging
logging.basicConfig(
    filename='sender.log',
    encoding='utf-8', 
    level=logging.DEBUG,
    format='%(asctime)s %(message)s', 
    datefmt='%d/%m/%Y %I:%M:%S %p')


# Server name and port
host = 'local host'
port = 5000
  
# create a socket at server side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
  
# bind the socket with server
# and port number
s.bind(('', port))

#Setting a 10 seconds timeout
s.settimeout(10)
# Connections allowed
s.listen(1)
  
# wait till a client accept
# connection
       
c, addr = s.accept()
if (addr):
       logging.info("Connection succesful")
       # display client address
       print("CONNECTION FROM:", str(addr))
       # send message to the client after
       # encoding into binary string
              
       msg = str(input("Message to send: "))
       logging.info("Original message: "+msg)
       msg = codecs.encode(msg,'rot13')
       logging.info("Codified message: "+ msg)

       c.send(msg.encode())
              
              # disconnect the server
       c.close()
       logging.info("Connection closed succesfully")
else:
       s.close()
       logging.info("Timeout. There was no connection")
