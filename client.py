import socket
import sys
from colorama import Fore
from random import choice

import colorama

colors_list = [Fore.BLACK, Fore.BLUE, Fore.GREEN, Fore.YELLOW, Fore.RED, Fore.WHITE]

argv = sys.argv
filename = argv[2]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', int(argv[1])))
print('connected to server')

file = open(filename, 'ab')
re = client.recv(1024)
count = 1
while re:
    file.write(re)
    re = client.recv(1024)
    print(choice(colors_list) + f'recived {len(re)}')
    count += 1

print(count)

client.close()
