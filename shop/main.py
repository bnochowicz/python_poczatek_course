# import orders
#
# your_order = orders.take_order()
# print(your_order)

from shop.orders import create_new_order, orders

def run_shop():
    print("Witaj w naszym sklepie!")
    product_name = input("Co chcesz zamówić? ")
    quantity = int(input("Ile szt/kg? "))

    result = create_new_order(product_name, quantity)
    if result is not None:
        total_price = result["total_price"]
        print(f"Łączny koszt wyniesie {total_price} PLN")

if __name__ == "__main__":
    option = None
    while option != 'X':
        run_shop()
        print(orders)
        option = input("Wybierz 'X' jeśli chcesz wyjsc ze sklepu lub cokolwiek innego zeby zlozyc zamowienie ponownie")
