sandwich_orders = ["pastrami", "tuna", "ham", "pastrami", "cheese", "pastrami", "turkey", "veggie"]
finished_sandwiches = []

# Remove all instances of "pastrami" from sandwich_orders
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

# Make sandwiches for the remaining orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("Finished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")

print("\nAll sandwiches have been made and served.")



