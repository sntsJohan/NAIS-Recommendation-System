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

# Global variables for UI elements
user_input_text = None
question_text = None
result_text = None
main_window = None

# Function to get the user input and display the next question or make a recommendation
def submit_answer():
    global current_question_index, user_input_text, question_text, result_text, main_window

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

        create_result_window(recommendation)

# Function to skip to the next question
def skip_question():
    global current_question_index
    if current_question_index < len(questions) - 1:
        current_question_index += 1
        ask_question()

# Function to ask the current question
def ask_question():
    global question_text, user_input_text
    question_text.config(state=tk.NORMAL)  # Enable text widget for editing
    question_text.delete("1.0", tk.END)
    question_text.insert(tk.END, questions[current_question_index])
    question_text.config(state=tk.DISABLED)  # Disable text widget after inserting question
    user_input_text.delete("1.0", tk.END)

# Function to create the main UI for answering questions
def create_main_ui():
    global user_input_text, question_text, result_text, main_window

    main_window = tk.Tk()
    main_window.title("Program Recommendation System")

    # Create a text widget for displaying the current question
    question_text = tk.Text(main_window, height=2, wrap=tk.WORD)
    question_text.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    question_text.config(state=tk.DISABLED)  # Disable text widget for editing

    # Create a text widget for user input
    user_input_text = scrolledtext.ScrolledText(main_window, width=40, height=10, wrap=tk.WORD)
    user_input_text.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    # Create a button to trigger the next question or recommendation
    submit_button = tk.Button(main_window, text="Submit Answer", command=submit_answer)
    submit_button.grid(row=2, column=0, pady=10, sticky="w")

    # Create a skip button to go to the next question
    skip_button = tk.Button(main_window, text="Skip Question", command=skip_question)
    skip_button.grid(row=2, column=0, pady=10, padx=100, sticky="w")

    # Create a text widget for displaying the recommendation
    result_text = scrolledtext.ScrolledText(main_window, width=40, height=5, wrap=tk.WORD)
    result_text.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    # Start by asking the first question
    ask_question()

    # Start the main loop for the main UI
    main_window.mainloop()

# Function to create the result window with the recommendation
def create_result_window(recommendation):
    result_window = tk.Tk()
    result_window.title("Recommendation Result")

    result_label = tk.Label(result_window, text=f"Based on your input, we recommend: {recommendation}", font=("Helvetica", 12))
    result_label.pack(padx=10, pady=10)

    result_window.mainloop()

# Function to create the welcome window
def create_welcome_window():
    global main_window

    welcome_window = tk.Tk()
    welcome_window.title("Welcome to the NAIS Recommendation System")

    welcome_label_text = "Welcome to the NAIS Recommendation System!\n\n" \
                         "We're here to help you choose between Information Technology (IT) and Computer Science (CS).\n" \
                         "Please click the 'Take Test' button to start the test."

    welcome_label = tk.Label(welcome_window, text=welcome_label_text, font=("Helvetica", 12), justify=tk.LEFT)
    welcome_label.pack(padx=10, pady=10)

    start_test_button = tk.Button(welcome_window, text="Take Test", command=start_test)
    start_test_button.pack(pady=10)

    welcome_window.mainloop()

# Function to start the test and close the welcome window
def start_test():
    global main_window
    create_main_ui()
    welcome_window.destroy()  # Close the welcome window

# Welcome message
welcome_message = "Welcome to the NAIS Recommendation System!\n\n" \
                  "We're here to help you choose between Information Technology (IT) and Computer Science (CS).\n" \
                  "Please click the 'Take Test' button to start the test."

# Start the program by creating the welcome window
create_welcome_window()
