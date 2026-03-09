from nlp_engine import get_response

print("AI Chatbot: Hello! Type 'quit' to exit.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Chatbot: Goodbye!")
        break

    response = get_response(user_input)
    print("Chatbot:", response)
