import csv
import os


# базовый класс автомобилей
class BaseCar:
    def __init__(self, car_type, photo_file_name, brand, carrying):
        self.car_type = car_type
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = carrying

    # получение расширения фото
    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


# легковой автомобиль
class Car(BaseCar):
    def __init__(self, car_type, photo_file_name, brand, carrying, passenger_seats_count):
        super().__init__(car_type, photo_file_name, brand, carrying)
        self.passenger_seats_count = passenger_seats_count


# грузовой автомобиль
class Truck(BaseCar):
    def __init__(self, car_type, photo_file_name, brand, carrying, body_width, body_height, body_length):
        super().__init__(car_type, photo_file_name, brand, carrying)
        self.body_width = body_width
        self.body_height = body_height
        self.body_length = body_length

    # объем автомобиля
    def get_body_volume(self):
        return self.body_height * self.body_length * self.body_width


# спецтехника
class SpecMachine(BaseCar):
    def __init__(self, car_type, photo_file_name, brand, carrying, extra):
        super().__init__(car_type, photo_file_name, brand, carrying)
        self.extra = extra


# получаем список автомобилей из файла
def get_car_list(csv_filename):
    car_list = []
    try:
        with open(csv_filename) as csv_fd:
            reader = csv.reader(csv_fd, delimiter=';')
            next(reader)  # пропускаем заголовок
            for row in reader:
                car = get_car(row)
                if car is not None:
                    car_list.append(car)

        return car_list
    except IOError:
        return car_list


# получение из строки экземпляра нужного класса
def get_car(row):
    car = None
    try:
        # создаем автомобили по типам
        # легковой
        if row[0] == 'car':
            car = Car(row[0], row[3], row[1], float(row[5]), int(row[2]))
        # грузовой
        elif row[0] == 'truck':
            # размер
            if row[4] == '':
                body_length = 0
                body_width = 0
                body_height = 0
            else:
                body_length = float(row[4].split('x')[0])
                body_width = float(row[4].split('x')[1])
                body_height = float(row[4].split('x')[2])
            car = Truck(row[0], row[3], row[1], float(row[5]), body_width, body_height, body_length)
        # спецтехника
        elif row[0] == 'spec_machine':
            car = SpecMachine(row[0], row[3], row[1], float(row[5]), row[6])
        else:
            car = None

        return car
    except (IndexError, ValueError):
        return None

