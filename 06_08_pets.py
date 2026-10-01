pet_0 = {
    "Type": "Dog",
    "Breed": "Golden Retriever",
    "Age": 3,
    "Owner": "John Doe"
}

pet_1 = {
    "Type": "Cat",
    "Breed": "Maine Coon",
    "Age": 5,
    "Owner": "Jane Smith"
}

pet_2 = {
    "Type": "Bird",
    "Breed": "Parrot",
    "Age": 2,
    "Owner": "Bob Johnson"
}

pets = [
    pet_0,
    pet_1,
    pet_2
]

for pet in pets:
    for key, value in pet.items():
        print(f"{key}: {value}")
    print()  # Print a blank line between each pet's information
    