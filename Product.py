class Product:

    def __init__(self, barCode, name, category, stock, price):
        self.barCode = barCode
        self.name = name
        self.category = category
        self.stock = stock
        self.price = price

    def printProduct(self):
        print("Name:", self.name)
        print("category:", self.category)
        print("stock:", self.stock)
        print("price:", self.price)

    def __str__(self):
        return str.format("{}:{} ({})",
                          self.barCode, self.name, self.stock)
