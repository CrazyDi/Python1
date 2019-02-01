import socket
import threading


def process_request(conn, addr):
    print("connected client:", addr)

    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data.decode("utf8"))


if __name__ == "__main__":
    with socket.socket() as sock:
        sock.bind(('127.0.0.1', 10001))
        sock.listen(socket.SOMAXCONN)

        while True:
            conn, addr = sock.accept()
            th = threading.Thread(target=process_request, args=(conn, addr))
            th.start()
