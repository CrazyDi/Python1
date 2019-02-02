import asyncio

STORAGE = {}

class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport: asyncio.transports.Transport):
        self.transport = transport

    def data_received(self, data):
        resp = self._process_data(data.decode())

        self.transport.write(resp.encode())

    def _process_data(self, data_str):
        print(data_str)
        data_list = data_str.split()

        if data_str.startswith("put"): # занесение значения в хранилище
            metric_name = data_list[1]
            metric_value = float(data_list[2])
            timestamp = int(data_list[3])
            print(metric_name)
            print(metric_value)
            print(timestamp)

            if metric_name in STORAGE: # если такой ключ уже есть в хранилище
                for idx, ts in enumerate(STORAGE[metric_name]): # поищем такой же timestamp
                    if ts[0] == timestamp: # и если нашли, удалим такую запись
                        del STORAGE[metric_name][idx]

                # print(self.storage)
                # теперь просто добавим значение в список
                STORAGE[metric_name].append((timestamp, metric_value))
                # print(self.storage)
                # и отсортируем
                STORAGE[metric_name].sort()
            else: # нет ключа
                STORAGE[metric_name] = [(timestamp, metric_value)]

            print(STORAGE)

            result_str = "ok\n\n"

        elif data_str.startswith("get"): # передача данных
            result_str = "ok\n"

            data_list = data_str.split()
            metric_name = data_list[1]

            if metric_name == "*":
                for metric_name in STORAGE:
                    for metric in STORAGE[metric_name]:
                        result_str += metric_name + ' ' + str(metric[1]) + ' ' + str(metric[0]) + '\n'
            elif metric_name in STORAGE:
                for metric in STORAGE[metric_name]:
                    result_str += metric_name + ' ' + str(metric[1]) + ' ' + str(metric[0]) + '\n'

            result_str += "\n"
        else:
            result_str = 'error\nErrorProtocol\n\n'

        return result_str


def run_server(host, port):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == "__main__":
    asyncio.run(run_server('127.0.0.1', 8888))