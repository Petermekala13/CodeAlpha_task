import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?", "Hi there! How can I help you?"]
    ],
    [
        r"what is your name\\??",
        ["I'm a chatbot created to assist you. You can call me Bot!", "I’m your virtual assistant. Call me Bot."]
    ],
    [
        r"how are you\\??",
        ["I'm just a bot, but I'm functioning as expected!", "I'm good, thank you! How can I assist you?"]
    ],
    [
        r"what can you do\\??",
        ["I can help you with basic tasks, answer questions, or just chat! What do you need?"]
    ],
    [
        r"(.*) created you\\??",
        ["I was created by a developer using Python!", "A developer who loves coding made me!"]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day!", "Bye! Take care!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand that. Can you rephrase?", "Can you elaborate on that?"]
    ]
]

def chatbot():
    print("Chatbot: Hi! I'm here to assist you. Type 'quit' to exit.")
    chatbot_instance = Chat(pairs, reflections)
    chatbot_instance.converse()

if __name__ == "__main__":
    nltk.download('punkt')  
    chatbot()
