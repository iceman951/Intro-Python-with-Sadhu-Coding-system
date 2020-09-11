discount_table = {"food" : 0.03, "medicine" : 0.01, "shoes" : 0.20}

def calculate_discount(product_type , price):
    discount_price = float(price)
    if discount_table.get(product_type) != None:
        discount_price = float(price) *( 1 - discount_table[product_type])
    return discount_price

product_type = input("Enter product type: ")
product_price = input("Enter price: ")
product_discount = calculate_discount(product_type,product_price)
print("Price after discount is {:.2f}".format(product_discount))