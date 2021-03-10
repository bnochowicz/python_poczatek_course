products = {
    "apple" : {
        "quantity" : 50,
        "price" : 5},
    "bread" : {
        "quantity" : 100,
        "price" : 2
    }
}

def update_product_quantity(prduct_name, ordered_quantity):
    products[prduct_name]["quantity"] -= ordered_quantity