print("Welcome to the rental car program!")
print("Let's get some information from you to help you rent a car.")

name = input("What is your name? ")
age = int(input("What is your age? "))
driver_license = input("Do you have a driver's license? (yes/no) ")

if age < 25:
    print("I'm sorry, but you must be at least 25 years old to rent a car.")
elif driver_license.lower() == "yes":
    print(f"Thank you, {name}. You are eligible to rent a car.")
else:
    print(f"Sorry, {name}. You are not eligible to rent a car.")








    