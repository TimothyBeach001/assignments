Pizza = ["Pepperoni", "Margherita", "Hawaiian"]

friend_pizzas = Pizza[:]

# add a new pizza to the original list

Pizza.append("BBQ Chicken")

# add different pizza to the friend's list

friend_pizzas.append("Vegetarian")

# prove that you have two separate lists

print("My favorite pizzas are:")
for pizza in Pizza:
    print(pizza)

print("\My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
