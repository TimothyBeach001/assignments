age = 4

if age < 2:
    print("Baby")
elif age in range(2, 4):
    print("Toddler") 
elif age in range(4, 13):
    print("Kid")
elif age >= 13 and age < 20:
    print("Teenager")
elif age >= 20 and age < 65:
    print("Adult")
else:
    print("Elder")


