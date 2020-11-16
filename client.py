from core import MySocket
import sys

address: tuple = ('127.0.0.1', 1115)

with MySocket() as socket:
    socket.connect(address)
    file = open('core.py','r')
    socket.send(file.read())
    response = socket.recieve(1024)
    print(response)
