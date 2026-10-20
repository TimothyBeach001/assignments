def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['Tim'] = first
    user_info['Beach'] = last
    return user_info

keyboard = build_profile('Tim', 'Beach', location='Dundalk', field='Computer Science')
print(keyboard)
