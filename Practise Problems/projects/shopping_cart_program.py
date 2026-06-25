

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: "))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")
print()

for i in foods:
    print(i)

for price in prices:
    total += price

print()
print(f"Your Total is ${total}")

