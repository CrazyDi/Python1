import socket

if __name__ == "__main__":
    HOST = '127.0.0.1'
    POST = 50007

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, POST))
        s.sendall(b'Hello world')
        data = s.recv(1024)
        print('Received', repr(data))
        s.sendall(b'Hello Kate')
        data = s.recv(1024)
        print('Received', repr(data))
