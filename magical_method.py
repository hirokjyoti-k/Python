class Magical_method:

    def __init__(self, message):
        self.message = message

    def __len__(self):
        return len(self.message)

    def __str__(self):
        return self.message

    def __repr__(self):
        return f"Magical_method(\"{self.message}\")"

    #operator overloading...
    def __add__(self, other):
        return f"{self.message} {other.message}"

m1 = Magical_method("Hello")
print(len(m1))

print(repr(m1))

#operator overloading...
m2 = Magical_method("World")
print(m1+m2)

