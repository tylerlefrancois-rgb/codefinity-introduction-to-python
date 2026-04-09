# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")
shelf_tuple = tuple(shelf)
apple_count = shelf_tuple.count("apples")
print("Number of Apples:", apple_count)
banana_index = shelf_tuple.index("bananas")
print("First Banana Index:", banana_index)
if apple_count < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")

grape_count = shelf_tuple.count("grapes")
if grape_count <= 1:
    print("Grapes need to be restocked.")
else:
    print("Grapes are suffieciently stocked.")

orange_index = shelf_tuple.index("oranges")

if "oranges" in shelf_tuple:
    print("Oranges are at index:", orange_index)
else:
    print("Oranges are out of stock.")