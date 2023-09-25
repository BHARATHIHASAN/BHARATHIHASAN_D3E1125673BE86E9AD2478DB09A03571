def linear_search_product(products, target_product):
    indices = []
    for index, product in enumerate(products):
        if product == target_product:
            indices.append(index)
    return indices



# Sample list of products
product_list = ["apple", "banana", "orange", "apple", "grape", "apple"]

# Target product to search for
target_product = "apple"

# Call the function
result = linear_search_product(product_list, target_product)

# Print the result
print(result)
