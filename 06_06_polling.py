poll = ["jen", "mike", "sarah", "edward", "phil"]

favorite_languages = {

    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",

}
for person in poll:
    if person in favorite_languages:
       print(f"Thank you {person.capitalize()} for taking the poll!")
    else:
        print(f"{person.capitalize()}, please take the poll!")
    
        



