# test equality and inequality with strings
string_1 = "dog"
string_2 = "cat"

print("Is string_1 == string_2? I predict False.")
print(string_1 == string_2)

print("Is string_1 != string_2? I predict True.")
print(string_1 != string_2)
# test using . loweer()
print("Is string_1 == string_1.lower()? I predict False.")
print(string_1 == string_1.lower())

# numerical test

number = 10
print("Is number == 10? I predict True.")
print(number == 10)
print("Is number == 10? I predict False.")
print(number != 10)

print("Is number > 10? I predict False.")
print(number > 10)

print("Is number < 10? I predict false.")
print(number < 10)


print("Is number >= 10? I predict True.")
print(number >= 10)

print("Is number <= 10? I predict True.")
print(number <= 10)

# and/or

print("Is number >= 10 AND even? I predict True")
print(number >= 10 and (number % 2 == 0))

print("Is number >= 10 AND odd? I predict False")
print(number >= 10 and (number % 2 != 0))

print("Is number >= 10 or odd? I predict True")
print(number >= 10 or (number % 2 != 0))

# in/not

list_1 = ["dog", "cat"]

print("Is 'duck' in list_1? I predict False")
print("duck" in list_1)

print("Is 'dog' in list_1? I predict True")
print("dog" in list_1)

print("Is 'dog' not in list_1? I predict False")
print("dog" not in list_1)






