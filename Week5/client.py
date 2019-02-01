import socket
import time


class ClientError(Exception):
    pass


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    def put(self, metric_name, metric_value, timestamp=None):
        """преобразовывает данные в строку и отправляет на сервер"""
        if timestamp is None:
            timestamp = str(int(time.time()))
        send_str = f"put {metric_name} {metric_value} {timestamp}\n"

        with socket.create_connection((self.host, self.port), timeout=self.timeout) as sock:
            sock.send(send_str.encode("utf8"))
            data = sock.recv(1024).decode("utf8")

        if data != "ok\n\n":
            raise ClientError

    def get(self, metric_name):
        """возвращает значения"""
        pass
