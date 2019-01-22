import sys
import os
import tempfile

class File:
    """Класс файла"""

    def __init__(self, path):
        self.path = path
        self.current = 0

    def write(self, str):
        """Метод записи в файл"""

        with open(self.path, "a") as f:
            f.write(str)

    def __add__(self, object):
        result = File(os.path.join(tempfile.gettempdir(), 'result.txt'))
        for line in self:
            result.write(line)

        for line in object:
            result.write(line)

        return result


    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path) as f:
            result_list = f.readlines()
            if len(result_list) <= self.current:
                self.current = 0
                raise StopIteration
            else:
                result = result_list[self.current]
                self.current += 1
                return result

    def __str__(self):
        return self.path

if __name__ == "__main__":
    first = File(sys.argv[1])
    first.write('111\n')
    first.write('222\n')
    first.write('333\n')
    print(first)

    second = File(sys.argv[2])
    second.write('444\n')
    second.write('555\n')
    second.write('666\n')
    print(second)

    result = first + second
    print(result)




