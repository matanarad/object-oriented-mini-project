from Product import Product
from Inventory import Inventory, InventoryEncoder
import json


class Storage:
    def inventoryDecoder(inventoryJson):
        for barCode in inventoryJson:
            productJson = inventoryJson[barCode]
            newProduct = Product(barCode,
                                 productJson['name'],
                                 productJson['category'],
                                 productJson['stock'],
                                 productJson['price'])
            Inventory.addToInventory(newProduct)

    def saveFile():
        json_object = json.dumps(Inventory.inventory, cls=InventoryEncoder)
        f = open("inventoryList.json", "w")
        f.write(json_object)
        f.close()

    def readFile():
        with open('./inventoryList.json') as json_file:
            inventoryJson = json.load(json_file)
        Storage.inventoryDecoder(inventoryJson)
