class Methods:

    def __init__(self, msg, num):
        self.msg = msg
        self.num = num

    def print_message(self):
        print(self.msg)

    @classmethod
    def print_number(cls, number):
        print(number)

    @staticmethod
    def print_all(msg):
        print(msg)

method = Methods("HollW",502)
method.print_message()

Methods.print_all("Hi")
Methods.print_number(45)