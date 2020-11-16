import socket
from typing import Any
import logging


logging.basicConfig(level=logging.INFO)

class MySocket():
    '''

    '''
    def __init__(self, sock: Any = None):
        if sock == None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, address: tuple) -> None:
        """

        """
        try:
            self.sock.connect(address)
        except:
            logging.error("[*] Failed to connect on %s:%d" % (address[0], address[1]))


    def bind(self, address: tuple) -> None:
        """

        """
        try:
            self.sock.bind(address)
            self.sock.listen(5)
        except:
            logging.error("[*] Failed to listen on %s:%d" % (local_host, local_port))
            logging.error("[*] Check for other listening sockets or correct permissions.")

    def send(self, msg: str) -> None:
        """

        """
        self.sock.send(msg.encode())

    def recieve(self, bytes_count: int) -> bytes:
        """

        """
        response = self.sock.recv(bytes_count)
        return response
   
    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.sock.close()

