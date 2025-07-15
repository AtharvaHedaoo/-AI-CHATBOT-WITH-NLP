import spacy

# Load English tokenizer, POS tagger, parser, NER
nlp = spacy.load("en_core_web_sm")

# Define basic intents and responses
responses = {
    "greet": ["Hello!", "Hi there!", "Hey!", "Hi! How can I help you?"],
    "bye": ["Goodbye!", "See you later!", "Bye! Take care."],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "name": ["I'm an AI chatbot powered by spaCy NLP."],
    "default": ["I'm not sure how to respond to that.", "Can you rephrase your question?"]
}

# Simple intent detection
def get_intent(text):
    text = text.lower()
    if "hello" in text or "hi" in text:
        return "greet"
    elif "bye" in text or "goodbye" in text:
        return "bye"
    elif "thank" in text:
        return "thanks"
    elif "your name" in text or "who are you" in text:
        return "name"
    else:
        return "default"

# Chat loop
def chatbot():
    print("Chatbot: Hello! Ask me anything. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break

        doc = nlp(user_input)
        intent = get_intent(doc.text)
        from random import choice
        response = choice(responses[intent])
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
