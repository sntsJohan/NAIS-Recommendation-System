import spacy
import tkinter as tk
from tkinter import scrolledtext

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Define sets of keywords related to IT and CS
it_keywords = {"information technology", "networking", "security", "database", "web development", "cloud computing", "system administration"}
cs_keywords = {"computer science", "programming", "algorithms", "software development", "artificial intelligence", "machine learning", "data science"}

# Questions and current question index
questions = [
    "What aspects of technology interest you the most?",
    "Are you more drawn to working with hardware, software, or both?",
    "Do you have a preference for creating applications or managing information systems?",
    "What programming languages or technologies are you familiar with or interested in?",
]
current_question_index = 0

# Function to get the user input and display the next question or make a recommendation
def get_user_input():
    global current_question_index

    # Get user input from the text widget
    user_input = user_input_text.get("1.0", tk.END)

    # Process the user input with spaCy
    doc = nlp(user_input.lower())

    # Initialize counters for IT and CS keywords
    it_count = sum(1 for token in doc if token.text in it_keywords)
    cs_count = sum(1 for token in doc if token.text in cs_keywords)

    # Display the recommendation in the result text widget
    result_text.delete("1.0", tk.END)

    # Display the recommendation or move to the next question
    if current_question_index < len(questions) - 1:
        current_question_index += 1
        ask_question()
    else:
        # Determine the program recommendation based on keyword counts
        if it_count > cs_count:
            recommendation = "Bachelor of Science in Information Technology (BSIT)"
        else:
            recommendation = "Bachelor of Science in Computer Science (BSCS)"

        result_text.insert(tk.END, f"Based on your input, we recommend: {recommendation}")

# Function to ask the current question
def ask_question():
    question_text.delete("1.0", tk.END)
    question_text.insert(tk.END, questions[current_question_index])
    user_input_text.delete("1.0", tk.END)

# Create the main window
window = tk.Tk()
window.title("Program Recommendation System")

# Create a text widget for displaying the current question
question_text = tk.Text(window, height=2, wrap=tk.WORD)
question_text.grid(row=0, column=0, padx=10, pady=10)

# Create a text widget for user input
user_input_text = scrolledtext.ScrolledText(window, width=40, height=10, wrap=tk.WORD)
user_input_text.grid(row=1, column=0, padx=10, pady=10)

# Create a button to trigger the next question or recommendation
next_button = tk.Button(window, text="Next", command=get_user_input)
next_button.grid(row=2, column=0, pady=10)

# Create a text widget for displaying the recommendation
result_text = scrolledtext.ScrolledText(window, width=40, height=5, wrap=tk.WORD)
result_text.grid(row=3, column=0, padx=10, pady=10)

# Start by asking the first question
ask_question()

# Start the main loop
window.mainloop()
