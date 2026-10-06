movie_tickets = int(input("How many movie tickets would you like to purchase? "))
if movie_tickets < 0:
    print("Invalid input. Please enter a non-negative number.")

age = int(input("What is your age? "))
if age < 0:
    print("Invalid input. Please enter a non-negative age.")

price_per_ticket = 10.00  # Base price for a movie ticket   
if age < 13:
    price_per_ticket = 7.00  # Discounted price for children under 13


total_cost = movie_tickets * price_per_ticket
print(f"The total cost for {movie_tickets} movie tickets is ${total_cost:.2f}.")

print(f"The ticket price is ${10.00:.2f} for adults and ${7.00:.2f} for children under 13.")



