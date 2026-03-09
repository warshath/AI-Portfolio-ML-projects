import json
import random

with open("intents.json") as file:
    data = json.load(file)

def get_response(user_input):
    user_input = user_input.lower()

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            if pattern in user_input:
                return random.choice(intent["responses"])

    return "I'm not sure how to respond to that."
