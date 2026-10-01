user = {'aienstein': {'first': 'albert', 'last': 'einstein'}, 'mcurie': {'first': 'marie', 'last': 'curie'}}

for username, user_info in user.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location'] if 'location' in user_info else 'Unknown'
    print(f"\n there full name is {full_name.title()} and are from {location.title()}.")
