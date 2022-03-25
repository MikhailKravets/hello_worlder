import socket

if __name__ == '__main__':
    sock = socket.socket()
    sock.bind(('', 8001))
    sock.listen(1)

    print("Waiting for connection...")

    conn, addr = sock.accept()
    print(f"Connected: {addr}")

    while True:
        data = conn.recv(8)
        print(f"Data received: {data}")

        if not data:
            break

        conn.sendall(data.upper())

    conn.close()
    print("Connection closed")
