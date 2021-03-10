# import orders
#
# your_order = orders.take_order()
# print(your_order)

from shop.orders import create_new_order

def run_shop():
    print("Witaj w naszym sklepie!")
    product_name = input("Co chcesz zamówić? ")
    quantity = int(input("Ile szt/kg? "))

    result = create_new_order(product_name, quantity)
    if result is not None:
        total_price = result["total_price"]
        print(f"Łączny koszt wyniesie {total_price} PLN")

if __name__ == "__main__":
    run_shop()