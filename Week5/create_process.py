from multiprocessing import Process


def f(name):
    print("hello", name)


class PrintProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print("hello", self.name)


if __name__ == "__main__":
    p = Process(target=f, args=("Bob",))
    p.start()
    p.join()

    p = PrintProcess("Mike")
    p.start()
    p.join()
