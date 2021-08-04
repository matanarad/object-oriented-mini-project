from Order import Order
from Product import Product
from Storage import Storage
from Inventory import Inventory
import json


def addNewItemToInventory():
    p1 = Product(input("barCode: "), input("name: "), input("Category: "),
                 input("amaount: "), input("price: "))
    Inventory.addToInventory(p1)


def main():
    Storage.readFile()
    # addNewItemToInventory()
    # p1 = Product("4", "cola", "drinks", 5, 10)
    # Inventory.addToInventory(p1)
    # Inventory.moveStock("4", -4)


main()
# # Inventory.getShortInStock(2)
# o1 = Order()
# o1.addToOrder("2")
# o1.addToOrder("1")
# o1.addToOrder("2")
# o1.printOrder()
# # o1.delFromOrder("2")
# o1.printOrder()
# Storage.saveFile()
