menu = ("crab legs , ice cream , salad , steak , chicken , shrimp , pasta , pizza , soup , dessert")
print("The buffet menu is:")
for food in menu:
    print(food)

try:
    menu[0] = "new value"
except TypeError:
    print("sorry, the menu can't be changed!")

new_menu = ("crab legs , ice cream , salad , steak , chicken , shrimp , pasta , pizza , soup , dessert")
print("The new/revised buffet menu is:")
for food in new_menu:
    print(food)




