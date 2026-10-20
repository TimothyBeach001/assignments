def send_messages(messages):
    """Print each message in the list and move it to a new list."""
    sent_messages = []
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)
    return sent_messages

messages = [
    "Hello!",   
    "How are you?",
    "Have a great day!",
]

sent_messages = send_messages(messages)
print("Archived messages:")
for message in sent_messages:
    print(message)
