# Ask the user to input a number and print all the multiples of ten up to that number.
number = int(input("Please enter a number: "))

for i in range(10, number + 1, 10):
    print(i)

if number % 10 == 0:
    print(f"{number} is a multiple of ten.")



