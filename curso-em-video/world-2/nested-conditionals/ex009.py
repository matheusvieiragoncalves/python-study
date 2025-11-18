# Exercise 009 - Nested Conditionals
# Write a program that calcule the value to be paid for a product, considering its normal price and payment condition:
# - Cash/Check: 10% discount
# - Card (immediate payment): 5% discount
# - Card (up to 2x): normal price
# - Card (3x or more): 20% interest

product_price: float = float(input("Enter with product price: R$ "))

select_option: str = input(
    "Enter with payment method (Cash/Check, Card Immediate, Card up to 2x, Card 3x or more): "
)

payment_methods: dict[str, float] = {
    "Cash/Check": 0.9,
    "Card Immediate": 0.95,
    "Card up to 2x": 1.0,
    "Card 3x or more": 1.2,
}

if payment_methods.get(select_option) is None:
    print("Invalid payment option")
    exit(1)

factor: float = payment_methods[select_option]


final_price: float = product_price * factor


print(f"Final price to be paid: R$ {final_price:.2f}")
