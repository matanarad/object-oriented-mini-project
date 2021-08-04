from json.encoder import JSONEncoder
from Product import Product


class InventoryEncoder(JSONEncoder):

    def default(self, o):
        return o.__dict__


class Inventory:

    inventory: dict[str, Product] = {}

    def getNamedList():
        namedList = []
        for key, i in Inventory.inventory.items():
            namedList.append(i.name)
        return namedList

    def addToInventory(product: Product):
        Inventory.inventory[product.barCode] = product

    def setStock(barCode, newStock):
        Inventory.inventory[barCode].stock = newStock

    def moveStock(barCode, amount):
        Inventory.inventory[barCode].stock += amount

    def getShortInStock(limit: int):
        reFillListDict = {}
        reFillList = []
        for barCode, product in Inventory.inventory.items():
            if float(product.stock) < limit:
                reFillListDict[barCode] = product
                reFillList.append(product.name)
        print(reFillListDict)
        print(reFillList)
        return reFillList
