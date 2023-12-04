import tkinter as tk
from tkinter import IntVar, messagebox
import random

class LikertScaleSurvey:
    def __init__(self, root):
        self.root = root
        self.root.title("Likert Scale Survey")

        self.courses_it = [
            "ITE 001 - Computer Programming 1",
            "ITE 012 - Computer Programming 2",
            "IT 004 - Web Systems and Technologies",
            "IT 005 - Integrative Programming and Technologies",
            "IT 006 - Networking 1",
            "IT 003 - Advanced Database Systems",
            "IT 009 - Systems Integration and Architecture 1",
            "IT 401 - Data Mining and Warehousing",
            "IT 001 - Information Assurance and Security 1",
            "IT 007 - Networking 2",
            "ITE 030 - Data Analytics",
            "IT 008 - Systems and Administration Maintenance",
            "IT 002 - Information Assurance and Security 2",
            "ITE 010 - Systems Integration and Architecture 2",
            "IT 016 - Event Driven Programming",
            "IT 015 - Introduction to Game Development",
            "IT 014 - Human Computer Interaction 2",
            "IT 011 - Integrative Programming Technologies 2",
            "IT 013 - Web Systems and Technologies 2",
            "CS 409 - Mobile Computing",
            "CS 002 - Object Oriented Programming",
            "ITE 404 - Introduction to Data Science in Python",
            "SAP 501 - Business Analytics Using SAP Business Warehousing",
            "ITE 405 - Applied Plotting, Charting, and Data Representation",
            "ITE 406 - Applied Text Mining and Applied Social Network Analysis"
        ]

        self.courses_cs = [
            "CS 201 - Data Structures and Algorithms",
            "CS 409 - Mobile Computing",
            "CS 002 - Object Oriented Programming",
            "ITE 404 - Introduction to Data Science in Python"
        ]

        # Shuffle the order of courses
        random.shuffle(self.courses_it)
        random.shuffle(self.courses_cs)

        self.current_course_idx = 0
        self.responses = []
        self.counter_it = 0
        self.counter_cs = 0

        self.create_widgets()

    def create_widgets(self):
        intro_label = tk.Label(self.root, text="Please indicate how you feel about each course on a scale from 1 to 5, where 1 is 'Not at all' and 5 is 'Extremely'.", font=("Helvetica", 12), pady=10)
        intro_label.grid(row=0, column=0, columnspan=6)

        self.label = tk.Label(self.root, text=self.courses_it[self.current_course_idx], font=("Helvetica", 14), pady=10)
        self.label.grid(row=1, column=0, columnspan=6)

        likert_var = IntVar()
        likert_var.set(0)  # Default value

        likert_labels = ["Not at all", "Slightly", "Neutral", "Moderately", "Extremely"]

        for scale_value, label_text in enumerate(likert_labels, start=1):
            label = tk.Label(self.root, text=label_text, padx=5)
            label.grid(row=2, column=scale_value, sticky=tk.W)

        for scale_value in range(1, 6):
            radio_button = tk.Radiobutton(
                self.root,
                text=str(scale_value),
                variable=likert_var,
                value=scale_value
            )
            radio_button.grid(row=3, column=scale_value, padx=5)

        next_button = tk.Button(self.root, text="Next Course", command=self.next_course)
        next_button.grid(row=4, column=2, pady=10)

        submit_button = tk.Button(self.root, text="Submit", command=self.submit_survey)
        submit_button.grid(row=4, column=3, pady=10)

        self.responses.append(likert_var)

    def next_course(self):
        self.current_course_idx += 1
        if self.current_course_idx < len(self.courses_it):
            if random.random() < 0.5:  # 50% chance to switch between IT and CS courses
                self.label.config(text=self.courses_it[self.current_course_idx])
            else:
                self.label.config(text=self.courses_cs[self.current_course_idx])
        else:
            self.label.config(text="Survey complete")

    def submit_survey(self):
        submitted_responses = [var.get() for var in self.responses]
        for response in submitted_responses:
            if self.current_course_idx < len(self.courses_it):
                self.counter_it += response
            else:
                self.counter_cs += response

        messagebox.showinfo("Survey Complete", f"Thank you for completing the survey!\n\nResults:\nBSIT Counter: {self.counter_it}\nBSCS Counter: {self.counter_cs}\n\nWe recommend you to take {'BSIT' if self.counter_it > self.counter_cs else 'BSCS'}.")

        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    survey_app = LikertScaleSurvey(root)
    root.mainloop()
