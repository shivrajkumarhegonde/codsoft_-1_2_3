from flask import Flask, render_template, request
from datetime import datetime
import re

app = Flask(__name__)

# Variable to store the user's name
user_name = None

@app.route("/")
def home():
    return render_template("chatbot.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    global user_name
    user_input = request.json.get("message", "").strip().lower()

    # Predefined generic greetings
    greetings = ["hi", "hello", "hey", "greetings"]

    # Handle user name input
    if user_name is None:
        if re.match(r"my name is\s+(\w+)", user_input, re.IGNORECASE):
            user_name = re.match(r"my name is\s+(\w+)", user_input, re.IGNORECASE).group(1).capitalize()
            return {"response": f"Nice to meet you, {user_name}!"}
        elif re.match(r"i am\s+(\w+)", user_input, re.IGNORECASE):
            user_name = re.match(r"i am\s+(\w+)", user_input, re.IGNORECASE).group(1).capitalize()
            return {"response": f"Nice to meet you, {user_name}!"}
        elif len(user_input.split()) == 1 and user_input.isalpha() and user_input not in greetings:
            user_name = user_input.capitalize()
            return {"response": f"Nice to meet you, {user_name}! How can I assist you today?"}

    # Personalized greetings
    if user_input in greetings:
        return {"response": f"Hello {user_name or 'there'}! How can I assist you today?"}

    # Responses to common questions
    if "your name" in user_input:
        return {"response": f"I'm ChatBot, your friendly assistant. What's your name?, {user_name or 'friend'}?"}
    elif "can you tell me which date today is" in user_input or "date" in user_input:
        current_date_day = datetime.now().strftime("%A, %d %B %Y")
        return {"response": f"Today's date is {current_date_day}, {user_name or 'friend'}."}
    elif "time" in user_input:
        current_time = datetime.now().strftime("%H:%M:%S")
        return {"response": f"The current time is {current_time}, {user_name or 'friend'}."}
    elif "what's your favorite food" in user_input or "favorite food" in user_input:
        return {"response": "I don't eat, but if I could, I'd imagine pizza and chocolate would be delightful!"}
    elif "what is ai" in user_input or "ai" in user_input:
        return {"response": "AI, or Artificial Intelligence, refers to systems designed to simulate human intelligence, enabling machines to perform tasks like learning, problem-solving, and decision-making."}

    # Friendly interactions
    elif "how are you" in user_input:
        return {"response": f"I'm just a bot, but I'm feeling great! How about you, {user_name or 'friend'}?"}
    elif user_input in ["i'm good", "i'm fine", "good", "fine", "not bad"]:
        return {"response": f"That's great to hear, {user_name or 'friend'}! How can I assist you today?"}
    elif "thank you" in user_input or "thanks" in user_input:
        return {"response": f"You're welcome, {user_name or 'friend'}! Let me know if there's anything else I can do for you."}
    elif "goodbye" in user_input or "bye" in user_input or "exit" in user_input:
        return {"response": f"Goodbye {user_name or 'friend'}! Have a nice day and take care!"}
    elif "hobbies" in user_input:
        return {"response": "I enjoy chatting with people, helping them out, and learning new things from our conversations!"}
    elif "tell me about yourself" in user_input:
        return {"response": f"I'm ChatBot, here to assist and chat with you. Ask me anything, {user_name or 'friend'}!"}
    elif "what can you do" in user_input:
        return {"response": "I can chat with you, answer your questions, and help you with various tasks. Just ask me anything!"}
    elif "do you have feelings" in user_input:
        return {"response": "I don't have feelings, but I aim to make our conversations enjoyable and helpful!"}
    elif "do you sleep" in user_input:
        return {"response": "I never sleep! I'm always here whenever you need assistance."}
    elif "can you sing" in user_input:
        return {"response": "I can't sing, but I can share some song recommendations if you'd like!"}
    elif "can you dance" in user_input:
        return {"response": "I wish I could dance, but I can certainly find some great dance videos for you!"}
    elif "what's your favorite color" in user_input:
        return {"response": "I don't see colors, but I hear blue is very calming!"}
    elif "do you have friends" in user_input:
        return {"response": "Everyone who chats with me is my friend, including you!"}

    # Error handling for unknown input
    else:
        return {"response": "I'm sorry, I didn't quite catch that. Can you rephrase or ask something else?"}

if __name__ == "__main__":
    app.run(debug=True)
