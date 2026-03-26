# The item's discount and stock status have been defined
discounted      = False
lowStock        = True

# Step 1: Combine the conditions to check if item is discounted or low in stock
movingProduct  = discounted or lowStock

# Step 2: promotion is True only if the item is NOT discounted and NOT low in stock
promotion       = not movingProduct

# Step 3: Print the eligibility status
print("Is the item eligible for promotion?", promotion)