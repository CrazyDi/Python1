# основной класс
class FileReader:
    # инициализация класса
    def __init__(self, file_path):
        self.file_path = file_path
        self.result = ''

    # чтение файла в строку
    def read(self):
        try:
            with open(self.file_path) as f:
                for line in f:
                    self.result = self.result + line.rstrip("\n")
        except IOError:
            self.result = ''
        finally:
            return self.result