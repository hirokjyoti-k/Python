class Laptop:
    def __init__(self, brand, model_name, price): #self represent object (model_name here)
        self.brand = brand
        self.model_name = model_name
        self.price = price
    
    def full_laptop_name(self):
        return f"{self.brand} {self.model_name}"


    def discounted_price(self, discount):
        return self.price - (self.price * (discount/100))

model_one = Laptop('Asus',"Vivibook 15", 56000)
print(model_one.full_laptop_name())
print(f"Price: {model_one.price}")
print(f"Discounted Price: {model_one.discounted_price(5)}")

