def send_messages(messages):
    """Print each message in the list and move it to a new list."""
    sent_messages = []
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)
    return sent_messages





