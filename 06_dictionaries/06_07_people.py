person_0 = {
    "First_name": "Tim",
    "Last_name": "Beach",
    "Age": 19,
    "City": "Baltimore",
}

person_1 = {
    "First_name": "Alice",
    "Last_name": "Smith",
    "Age": 25,
    "City": "New York",
}

person_2 = {
    "First_name": "Bob",
    "Last_name": "Johnson",
    "Age": 30,
    "City": "Los Angeles",
}

people = [
    person_0,
    person_1,
    person_2
]

for person in people:
    for key, value in person.items():
        print(f"{key}: {value}")
    print()  # Print a blank line between each person's information