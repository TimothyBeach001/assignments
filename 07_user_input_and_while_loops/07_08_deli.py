sandwich_orders = ['tuna', 'ham', 'cheese', 'turkey', 'veggie']
finished_sandwiches = []    

while sandwich_orders:
      current_sandwich = sandwich_orders.pop()
      print(f"I made your {current_sandwich} sandwich.")
      finished_sandwiches.append(current_sandwich)

print("Finished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")

print("\nAll sandwiches have been made and served.")


