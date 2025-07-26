import random

# Define a dictionary of intents
intents = {
    "greetings": {
        "patterns": ["hello", "hi", "hey"],
        "responses": ["Hi, how are you?", "Hello! How can I help you?", "Hey! What's up?"]
    },
    "goodbye": {
        "patterns": ["bye", "see you later"],
        "responses": ["See you later!", "Bye! Have a great day!"]
    },
    "morning": {
        "patterns": ["good morning", "happy morning", "pleasent morning"],
        "responses": ["Have a nice day!", "Have a great day!", "hope you're having a great day to start!"]
    },
   "quote": {
        "patterns": ["tell some quote"],
        "responses": ["Small Steps Today, Big Impact Tomorrow "]
    },
    "mean": {
        "patterns": ["quote meaning"],
        "responses": ["taking small,achievable actions now will build momentum over a time"]
    },
    "could you help me": {
        "patterns": ["could you help me"],
        "responses": ["Absolutely! I'd be happy to help with whatever you need!😊"]
    },


}

def match_intent(input_text):
    for intent, values in intents.items():
        for pattern in values["patterns"]:
            if pattern in input_text.lower():
                return intent
    return None

def respond(intent):
    if intent is not None:
        return random.choice(intents[intent]["responses"])
    else:
        return "I didn't understand that. Can you please rephrase?"

def chatbot():
    print("Welcome to the chatbot! Type 'quit' to exit.")
    while True:
        input_text = input("You: ")
        if input_text.lower() == "quit":
            break
        intent = match_intent(input_text)
        response = respond(intent)
        print("Chatbot: ", response)

chatbot()

