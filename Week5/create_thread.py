from threading import Thread


def f(name):
    print("hello", name)


class PrintThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print("hello", self.name)


if __name__ == "__main__":
    th = Thread(target=f, args=("Bob",))
    th.start()
    th.join()

    th1 = PrintThread("Mike")
    th1.start()
    th1.join()
