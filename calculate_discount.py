def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Apply the discount
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        # No discount applied, return the original price
        return price

# Prompt the user for input
price = float(input("Enter the original price of the item: $"))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate and print the final price
final_price = calculate_discount(price, discount_percent)

# Display the final price
print(f"The final price is: ${final_price:.2f}")