#  Q19. Compare Two Objects
#  Create a class Product with a constructor that accepts name and price.
#  Create two objects and a method that compares their prices and displays which product is more expensive.
class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def compare(self,other):
        if(self.price > other.price):
            print(self.name," is more expensive")
        else:
            print(other.name," is more expensive")

p1 = Product("Iphone",50000)
p2 = Product("Samsung",35000)
p1.compare(p2)

