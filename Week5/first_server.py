import socket

if __name__ == "__main__":
    HOST = ''
    PORT = 50007

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)

        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)

            while True:
                data = conn.recv(1024)
                print(data)
                if not data:
                    break
                conn.sendall(data)
