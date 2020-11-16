from core import MySocket


address: tuple = ('127.0.0.1', 2555)

with MySocket() as socket:
    socket.bind(address)

    while True:
        client_socket, address = socket.sock.accept()

        request = client_socket.recv(1024)

        print(f'{address[0]} sent {request}')
        client_socket.send(b'OK')
