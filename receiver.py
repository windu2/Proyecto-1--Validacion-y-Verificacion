
import socket
import logging
import codecs
import time


#logging Config
logging.basicConfig(
    filename='receiver.log',
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

connected = True
current_time = time.time()
connection_timeout = current_time + 10

while current_time < connection_timeout:
    try:
        s.connect(('127.0.0.1', port))
        connected = True
        break

    except Exception as e:
        connected = False

    current_time = time.time() 

if not connected:
    logging.error('Connection Timeout')



if(connected): 
  
    # receive message string from
    # server, at a time 1024 B
    msg = s.recv(1024)
    

    # repeat as long as message
    # string are not empty
    while msg:
        logging.info('Message received')
        final_msg = msg.decode()
        logging.info("INPUT -> "+ final_msg)
        final_msg = codecs.decode(final_msg , 'rot_13')
        logging.info("OUTPUT -> "+ final_msg)
        print('Received:' + final_msg)
        logging.info('Message showed')
        msg = s.recv(1024)


     
# disconnect the client
try:
    s.close()
    logging.info('Disconnected Suscessfully')
except Exception as e:
    logging.error('Disconnection Error')

    

