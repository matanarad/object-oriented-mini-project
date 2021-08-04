from Inventory import Inventory
from Product import Product


class Order:
    def __init__(self):
        self.cartList: list[Product] = []
        self.amountList: list[int] = []
        self.customerName = ""

    def prodactExistInOreder(self, barCode):
        for i in self.cartList:
            if i.barCode == barCode:
                return True
        return False

    def getPosByBarCode(self, barCode):
        pos = 0
        for i in self.cartList:
            if i.barCode == barCode:
                return pos
            pos += 1

    def getPriceByName(self, name):
        pos = 0
        for i in self.cartList:
            if i.name == name:
                return Inventory.inventory[pos].price
            pos += 1

    def addToOrder(self, barCode):
        if Inventory.inventory[barCode].stock != 0:
            if self.prodactExistInOreder(barCode):
                posToInsert = Order.getPosByBarCode(self, barCode)
                if len(self.amountList) - posToInsert >= 0:
                    self.amountList[posToInsert] += 1
                else:
                    print("error")
            else:
                self.cartList.append(Inventory.inventory[barCode])
                self.amountList.append(1)
            Inventory.inventory[barCode].stock -= 1
        else:
            print("out of stock")

    def delFromOrder(self, barCode):
        posToCheck = Order.getPosByBarCode(self, barCode)
        if self.amountList[posToCheck] > 1:
            self.amountList[posToCheck] -= 1
            Inventory.inventory[barCode].stock += 1
        else:
            self.cartList.remove(Inventory.inventory[barCode])
            Inventory.inventory[barCode].stock += 1

    def printOrder(self):
        sum = 0
        idx = 0
        for p in self.cartList:
            posOfAmount = Order.getPosByBarCode(self, p.barCode)
            sum += p.price * self.amountList[posOfAmount]
            idx += 1
            print(
                "Product name: {}, barCode: {}, price: {}$ - X{}"
                .format(p.name, p.barCode, p.price,
                        self.amountList[posOfAmount]))
        print("Total price: {}$".format(sum))
        return sum
