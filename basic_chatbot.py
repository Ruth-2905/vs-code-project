# basic chatbot

print("Hello! I am a simple chatbot. Type 'bye' to exit.")

while True:
    user = input("You: ")

    if user.lower() in ["bye", "exit", "quit"]:
        print("Chatbot: Goodbye ")
        break

    # simple rule based responses
    if "hello" in user.lower():
        print("Chatbot: Hello there! How can I help you?")
    elif "work" in user.lower():
        print("Chatbot: I don't know your work yet, but you can tell me about it")
    elif "name" in user.lower():
        print("Chatbot: My name is Basic Chatbot")
    else:
        print("Chatbot: I am not sure I understand you, can you rephrase?")
