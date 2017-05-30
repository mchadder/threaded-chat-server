HOST=''
PORT=25002
INIT_MSG=b'Welcome to Chadders Chat Server\n'
RESPONSES={"Hi":b"Hello there\n"}
def server_handler(conn):
  while True:
    msg = conn.recv(1024).strip()
    msg = str(msg, 'utf-8')
    try: 
      conn.send(RESPONSES[msg])
    except Exception as e:
      conn.send(b"I don't know what that means\n")

from socket import *
from threading import Thread

try:
  s = socket(AF_INET, SOCK_STREAM)
  s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) 
  s.bind((HOST,PORT))
  s.listen(5)
  while True:
    conn,addr = s.accept()
    conn.send(INIT_MSG)
    Thread(target=server_handler, args=(conn,), daemon=None).start()
finally:
  print("\nCleaning up!")
  s.shutdown(SHUT_RDWR)
  s.close()
  try:
    conn.close()
  except NameError:
    pass

