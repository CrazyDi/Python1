import socket
# import time

if __name__ == "__main__":
    #  sock = socket.socket()
    #  sock.connect(("127.0.0.1", 10001))
    #   sock = socket.create_connection(('127.0.0.1', 10001))
    # try:
    with socket.create_connection(('127.0.0.1', 10001), 5) as sock:
        sock.sendall('bla'.encode("utf8"))
    # except:
    #   print("open connection data error")
    #  sock.close()
