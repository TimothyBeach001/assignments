# Write a program that asks the user to input a list of pizza toppings
# and then prints each topping on a separate line.

# Ask the user to input a list of pizza toppings
toppings = input("Please enter the pizza toppings (comma-separated): ").split(",")

# Print each topping on a separate line
for topping in toppings:
    topping = topping.strip()
    if topping:
        print(topping)

print("Thank you for your input! Enjoy your pizza!")


