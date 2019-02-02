import asyncio


class ClientServerProtocol(asyncio.Protocol):
    def __init__(self):
        self.transport = None

    def connection_made(self, transport: asyncio.transports.Transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        print('Data received: {!r}'.format(message))

        message = 'ok\n\n'
        print('Send: {!r}'.format(message))
        data = message.encode()
        self.transport.write(data)


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