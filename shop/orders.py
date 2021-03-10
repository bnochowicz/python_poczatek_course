# import products_store
#
# def take_order():
#     product_choose = input("Podaj nazwę produktu, który chcesz wybrać: ")
#     if product_choose is not None:
#         quantity_choose = input("Podaj ilość: ")
#         order = []
#         order += products_store.products_list[product_choose]
#         order += quantity_choose
#         # order += products.products_list[product_choose][1]
#         return order
#     else:
#         print("Błą∂")
#
#
from shop.products_store import products, update_product_quantity

# orders = [
#     {
#         "product" : "bread",
#         "quantity" : 10,
#         "total_price" : 20
#     }
# ]

orders = []

def create_new_order(product_name, quantity):
    price = products[product_name]["price"]
    available_quantity = products[product_name]["quantity"]

    if available_quantity < quantity:
        print("Nie mamy tyle towaru!")
        return None


    total_price = price * quantity

    new_order = {
        "product" : product_name,
        "quantity" : quantity,
        "total_price" : total_price
    }
    update_product_quantity(product_name, quantity)
    orders.append(new_order)
    return new_order