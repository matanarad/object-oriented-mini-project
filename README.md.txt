function to use in main:
manager side:

1. addNewItemToInventory() -> this function will daa new item to inventory file base on user input
2. moveStock(barCode, amount) -> this function will change the stock of a prodact by barCode and amount to change
3. setStock(barCode, newStock) -> this function will set the stock of a prodact to specific number
4. getShortInStock(limit: int) -> this function will print a list of prodact that their stock is under a number the user input

costomer side:

1.orderName = Order() -> create new order
2.orderName.addToOrder(barCode) -> add item to cart by barCode
3.orderName.delFromOrder(barCode) -> del item from cart by barCode
4.orderName.printOrder() -> print order details