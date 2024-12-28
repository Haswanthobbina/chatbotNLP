import os
import nltk
import ssl
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Setting up SSL and NLTK
ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download('punkt')

# Intents for the chatbot
intents = [
    {
        "tag": "greeting",
        "patterns": [
            "Hi",
            "Hello",
            "Hey",
            "How are you",
            "What's up"
        ],
        "responses": [
            "Hi there",
            "Hello",
            "Hey",
            "I'm fine, thank you",
            "Nothing much"
        ]
    },
    {
        "tag": "goodbye",
        "patterns": [
            "Bye",
            "See you later",
            "Goodbye",
            "Take care"
        ],
        "responses": [
            "Goodbye",
            "See you later",
            "Take care"
        ]
    }
]

# Setting up the ML model
vectorizer = TfidfVectorizer()
clf = LogisticRegression(random_state=0, max_iter=10000)

tags = []
patterns = []
for intent in intents:
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(pattern)

x = vectorizer.fit_transform(patterns)
y = tags
clf.fit(x, y)

def chatbot(input_text):
    input_text = vectorizer.transform([input_text])
    tag = clf.predict(input_text)[0]
    for intent in intents:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            return response
import csv
import datetime
import nltk
counter = 0

def main():
    global counter
    st.title("HASWANTH's CHATBOT")
    menu = ["Home", "Conversation History", "About"]
    choice = st.sidebar.selectbox("Menu", menu)


    if choice == "Home":
        st.write("Hello! welcome namastey vanakkam , HASWANTH fells bored ask something to his BOT by pressing Enter!")
        st.write("                                                                                                                                    ")
        st.write("                                                                                                                                    ")
        st.write("                                                                                                                                    ")
        st.write("                                                                                                                                    ")
        st.write("                                                                                                                                    ")


    # Adding a select slider
    if choice == "Home":
        mood = st.select_slider("How are you feeling today?",options=["Sad", "Neutral", "Happy", "Excited"],value="Neutral",)
        st.write(f"You're feeling: {mood}")
    

        # Ensure chat log file exists
        if not os.path.exists('chat_log.csv'):
            with open('chat_log.csv', 'w', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['User Input', 'Chatbot Response', 'Timestamp'])

        counter += 1
        user_input = st.text_input("YOU:", key=f"user_input_{counter}")

        if user_input:
            user_input_str = str(user_input)  # Corrected variable assignment
            response = chatbot(user_input)  # Corrected function call (chatbot, not Chatbot)
            st.text_area("Chatbot:", value=response, height=120, max_chars=None, key=f"chatbot_{counter}")  # Corrected syntax (value= , height=)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Append conversation to chat log
            with open('chat_log.csv', 'a', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)  # Corrected typo (csv.writer, not csv.wrwiter)
                csv_writer.writerow([user_input_str, response, timestamp])

            if response.lower() in ['goodbye', 'bye']:  # Corrected indentation
                st.write("Thank you for chatting with me. Have a great day!")
                st.stop()
                counter = 0  # Reset counter

                
    elif choice == "Conversation History":
        st.write("### Conversation History")
        if os.path.exists('chat_log.csv'):
            with open('chat_log.csv', 'r', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)
                history = list(csv_reader)
                if len(history) > 1:
                    for row in history[1:]:
                        st.write(f"**You:** {row[0]}")
                        st.write(f"**Bot:** {row[1]}")
                        st.write(f"*Timestamp:* {row[2]}")
                else:
                    st.write("No conversation history yet.")
        else:
            st.write("No conversation history yet.")

    elif choice == "About":
        st.write("### About")
        st.write("This is a chatbot project created by **Haswanth**, a student pursuing a degree at Sathyabama University.")
        st.write("The chatbot is designed using Python, Streamlit, and Machine Learning techniques such as TF-IDF and Logistic Regression.")
        st.write("### Key Features:")
        st.write("- Intuitive user interface powered by Streamlit.")
        st.write("- Logs conversations for review in a CSV file.")
        st.write("- Supports easy customization of intents and responses.")
        st.write("### Future Enhancements:")
        st.write("- Add more intents to handle diverse user inputs.")
        st.write("- Integrate advanced NLP models for improved accuracy.")
        st.write("### Contact:")
        st.write("For any queries or feedback, obbinahaswanth@gmail.com feel free to reach out to Haswanth.")
if __name__ == '__main__':
    main()

    
    
