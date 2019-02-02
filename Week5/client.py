import socket
import time


class ClientError(Exception):
    pass

class ClientSocketError(Exception):
    pass

class ClientProtocolError(Exception):
    pass


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = socket.create_connection((self.host, self.port), timeout=self.timeout)

    def put(self, metric_name, metric_value, timestamp=None):
        """преобразовывает данные в строку и отправляет на сервер"""
        if timestamp is None:
            timestamp = str(int(time.time()))
        send_str = f"put {metric_name} {metric_value} {timestamp}\n"

        self.sock.send(send_str.encode("utf8"))
        data = self.sock.recv(1024).decode("utf8")

        if data != "ok\n\n":
            raise ClientError

    def get(self, metric_name):
        """возвращает значения"""
        send_str = 'get ' + metric_name + '\n'
        self.sock.send(send_str.encode("utf8"))
        data = self.sock.recv(1024).decode("utf8")
        data_list = data.split('\n')
        if data_list[0] != "ok":
            raise ClientError

        data_list = data_list[1:]
        result = {}
        for s in data_list:
            if s != '':
                s_list = s.split()

                metric_name = s_list[0]
                metric_value = float(s_list[1])
                timestamp = int(s_list[2])
                if metric_name in result:
                    metric_list = result[metric_name]
                    metric_list.append((timestamp, metric_value))
                    metric_list.sort()
                else:
                    metric_list = [(timestamp, metric_value)]

                result[metric_name] = metric_list

        return result

    def Close(self):
        self.sock.close()


def _main():
    # проверка работы клиента
    client = Client("127.0.0.1", 8888, timeout=5)
    client.put("test", 0.5, timestamp=1)
    client.put("test", 2.0, timestamp=2)
    client.put("test", 0.5, timestamp=3)
    client.put("load", 3, timestamp=4)
    client.put("load", 4, timestamp=5)
    print(client.get("*"))

    client.Close()

if __name__ == "__main__":
    _main()