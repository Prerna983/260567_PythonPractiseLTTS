# Write Python code that asks a user how many pizza slices they want.
# The pizzeria charges Rs 123.00 a slice.
# If user order even number of slices, price per slice is Rs 120.00.
# Print the total price depending on how many slices user orders.

n = int(input("Enter number of pizza slices you want: "))
if n % 2 == 0:
    cost = 120 * n
else:
    cost = 123 * n

print("Total cost = ", cost)
