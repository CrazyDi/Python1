class Value():
    def __init__(self):
        self.amount = None

    def __get__(self, obj, obj_type):
        return self.amount

    def __set__(self, obj, value):
        value = value - value * obj.commission
        self.amount = value


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission