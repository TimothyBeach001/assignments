def display_message():
	print("I am learning about functions in Python.")


display_message()

def favorite_book():
    print("One of my favorite books is 'The Great Gatsby'.")

favorite_book()

book_title = input("What is your favorite book? ")
print(f"Your favorite book is '{book_title}'.")

def make_shirt(size="Large", message="I love Python"):
	print(f"The shirt size is {size} and the message is '{message}'.")


make_shirt("Large", "I love Python")

print("\nMaking a shirt with default size and message:")
make_shirt("Medium", "Python is awesome!")

arguments = {"size": "Small", "message": "Python is great!"}
make_shirt(**arguments)


