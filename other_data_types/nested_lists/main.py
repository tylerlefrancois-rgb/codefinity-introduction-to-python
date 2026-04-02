vegetables = ["tomatoes", "potatoes", "onions"]

# 1. Remove onions
vegetables.remove("onions")

# 2. Add carrots only if missing
if "carrots" not in vegetables:
    vegetables.append("carrots")

# 3. Add cucumbers only if missing
if "cucumbers" not in vegetables:
    vegetables.append("cucumbers")

# 4. Sort and print
vegetables.sort()
print("Updated Vegetable Inventory:", vegetables)