import socket

if __name__ == '__main__':
    sock = socket.socket()
    sock.connect(('localhost', 8001))
    sock.send(b'hello, world!')

    data = sock.recv(1024)

    print(data)
    sock.close()
