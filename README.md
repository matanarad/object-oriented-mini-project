Project goals:

    Demonstrate knowledge in Python and in object-oriented programming
    All code is written in Python and the style guide is PEP8
    The objects used are
        - Product
        - Inventory
        - Shopping Cart

General description:

    The purpose of the code is to demonstrate a store management system.
    From the side of the store owner and his control over the inventory of the store.
    And also from the side of the customer who wants to buy products in the store.

manager side:

    1. addNewItemToInventory() -> This function will add new item to inventory file base on user input
    2. moveStock(barCode, amount) -> This function will change the stock of a prodact by barCode and amount to change
    3. setStock(barCode, newStock) -> This function will set the stock of a prodact to specific number
    4. getShortInStock(limit: int) -> This function will print a list of prodact that their stock is under a number the user input

costomer side:

    1.orderName = Order() -> Create new order
    2.orderName.addToOrder(barCode) -> Add item to cart by barCode
    3.orderName.delFromOrder(barCode) -> Delete item from cart by barCode
    4.orderName.printOrder() -> Print order details

To use any of the functions uncomment the desired line in main.py file.
