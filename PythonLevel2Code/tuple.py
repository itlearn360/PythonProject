# Step 1: Create tuples for each product
product1 = ("Sneakers", 79.99, 25)
product2 = ("T-shirt", 19.99, 50)
product3 = ("Jeans", 39.99, 15)

# Step 2: Print out the product details
products = [product1, product2, product3]

for product in products:
    name, price, stock = product
    print(f"Product: {name}, Price: ${price}, Stock: {stock} units")

