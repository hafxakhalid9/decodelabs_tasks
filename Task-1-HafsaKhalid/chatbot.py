def simple_chatbot():
    print("Bot: Hello! I am your simple rule-based assistant.")
    print("Bot: Type 'bye' or 'exit' whenever you want to stop chatting.\n")
    
    # 1. Run in a continuous loop
    while True:
        # Get input from user and normalize it (convert to lowercase and trim spaces)
        user_input = input("You: ").lower().strip()
        
        # 2. Check for exit commands first
        if user_input in ["bye", "exit", "quit"]:
            print("Bot: Goodbye! Have a great day!")
            break  # Exit the infinite loop
            
        # 3. Handle greetings
        elif user_input in ["hello", "hi", "hey"]:
            print("Bot: Hello there! How can I help you today?")
            
        # 4. Predefined questions/answers
        elif "how are you" in user_input:
            print("Bot: I'm just a computer program, but I'm doing great! How about you?")
            
        elif "your name" in user_input:
            print("Bot: My name is RuleBot. I operate on simple Python conditions.")
            
        elif "help" in user_input:
            print("Bot: I can answer greetings, tell you my name, or say goodbye.")
            
        # 5. Catch-all fallback response
        else:
            print("Bot: I'm sorry, I don't understand that yet. Try asking 'help'.")

# Run the chatbot function
if __name__ == "__main__":
    simple_chatbot()