def make_shirt(size="Large", message="I love Python"):
	print(f"The shirt size is {size} and the message is '{message}'.")


make_shirt("Large", "I love Python")

print("\nMaking a shirt with default size and message:")
make_shirt("Medium", "Python is awesome!")

arguments = {"size": "Small", "message": "Python is great!"}
make_shirt(**arguments)



