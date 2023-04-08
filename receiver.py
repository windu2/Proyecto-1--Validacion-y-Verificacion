
import socket
import logging
import codecs


#logging Config
logging.basicConfig(
    filename='example.log',
    encoding='utf-8', 
    level=logging.DEBUG,
    format='%(asctime)s %(message)s', 
    datefmt='%d/%m/%Y %I:%M:%S %p')
  
# take the server name and port name
  
host = 'local host'
port = 5000
  
# create a socket at client side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
  
# connect it to server and port
# number on local computer.

connected = TRUE
try:
    s.connect(('127.0.0.1', port))

except Exception as e:
    logging.error('Connection Error')
    connected = FALSE



if(connected): 
  
    # receive message string from
    # server, at a time 1024 B
    msg = s.recv(1024)
    logging.info('Message received')

    # repeat as long as message
    # string are not empty
    while msg:
        final_msg = msg.decode()
        final_msg = codecs.decode(final_msg , 'rot_13')
        print('Received:' + final_msg)
        logging.info('Message showed')
        msg = s.recv(1024)


     
# disconnect the client
try:
    s.close()
    logging.info('So should this')
except Exception as e:
    logging.error('Disconnection Error')

    

