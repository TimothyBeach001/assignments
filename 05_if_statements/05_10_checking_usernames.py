current_users = {"admin", "micheal", "Kitty", "JOHN", "tom"}

new_users = ["John", "TOM", "Skye", "Gina", "Carl"]

current_users_lowered = [username.lower() for username in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lowered:
       print(f"{new_user} is already taken!")
       continue
    print(f"{new_user} is available!")



