import socket
import os
import sys
from colorama import Fore
from random import choice

colors_list = [Fore.BLACK, Fore.BLUE, Fore.GREEN, Fore.YELLOW, Fore.RED, Fore.WHITE, Fore.CYAN, Fore.MAGENTA]

argv = sys.argv
filename = argv[2]
filesize = os.path.getsize(filename)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', int(argv[1])))
server.listen(1)
print('server started')

conn, addr = server.accept()
print('client connected')

file = open(filename, 'rb')
fileContents = file.read(1024)
count = 1
while fileContents != bytes():
    conn.send(fileContents)
    print(choice(colors_list) + f'sended {len(fileContents)} - {count}')
    fileContents = file.read(1024)
    count += 1

print(count)

print('file sended')
server.close()