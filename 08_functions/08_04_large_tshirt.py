def make_shirt(size="Large", message="I love Python"):
	print(f"The shirt size is {size} and the message is '{message}'.")


make_shirt("Large", "I love Python")

print("\nMaking a shirt with default size and message:")
make_shirt("Medium", "I love Python!")

arguments = {"size": "Small", "message": "I love Python!"}
make_shirt(**arguments)




