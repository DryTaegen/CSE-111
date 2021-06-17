from datetime import datetime 

# Determine time
current = datetime.now()
weekday = current.isoweekday()
cart_items = 0
cost = "None"
while cost.lower() != "done":
    cost = input("What is the cost of the item? ")
    try:
        quantity = float(input("How many of those are you buying? "))
        an_item = float(cost) * quantity
        cart_items += an_item
        print(f"Your cart total is {cart_items}.")
        print()
    except ValueError:
        continue

# Cart inputs
#cart_items = float(input("How much is the subtotal? "))
sales_tax = .06 * cart_items



# Discount Check
if weekday == 2 or weekday == 3:
    if cart_items > 50:
        #offer the coupon

        new_cart_items = cart_items * .9
        sales_tax = .06 * new_cart_items
        cart_total = new_cart_items + sales_tax
        print(f"sales tax: {sales_tax:.2f}")
        print(f"Your discounted price is {cart_total:.2f}")
        cart_total = cart_items + sales_tax

    else:
        #("no coupon")
        cart_total = cart_items + sales_tax
        print(f"sales tax: {sales_tax:.2f}")
        print(f"Your total is {cart_total:.2f}")
        x = 50 - cart_total
        print(f"If you buy ${x:.2f} more of things you can get a 10% discount.")
else:
    #("no coupon")
    cart_total = cart_items + sales_tax
    print(f"sales tax: {sales_tax:.2f}")
    print(f"Your total is {cart_total:.2f}")
    