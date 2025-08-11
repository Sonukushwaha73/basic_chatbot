
def chatbot():
    print("Welcome to Simple Chatbot! (type 'exit' to quit)")
    while True:
        user_input = input("You: ").strip().lower()  # Take user input and normalize
        if user_input == "exit":
            print("Chatbot: Goodbye! Have a nice day.")
            break
        elif user_input == "hello":
            print("Chatbot: Hi!")
        elif user_input == "how are you":
            print("Chatbot: I am fine, thanks!")
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: Sorry, I don't understand that.")

chatbot()
