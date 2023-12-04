import tkinter as tk
from tkinter import IntVar, messagebox
import random

class LikertScaleSurvey:
    def __init__(self, root):
        self.root = root
        self.root.title("Likert Scale Survey")

        self.courses_it = [
            "Introduction to Human Computer Interaction",
            "Human Computer Interaction 2",
            "Data Structures and Algorithms",
            "Web Systems and Technologies",
            "Modern Biology",
            "Applied Statistics",
            "Information Management",
            "Platform Technologies",
            "Integrative Programming and Technologies",
            "Quantitative Methods (Including Modeling and Simulation)",
            "Networking",
            "Advanced Database Systems",
            "Systems Integration and Architecture 1",
            "Data Mining and Warehousing",
            "Information Assurance and Security 1",
            "Networking",
            "Data Analytic",
            "Social and Professional Issues",
            "Systems Administration and Maintenance",
            "Information Assurance and Security 2",
            "Systems Integration and Architecture 2"
        ]

        self.courses_cs = [
            "Number Theory",
            "Symbolic Logic",
            "Differential Calculus",
            "Principles of Programming Languages",
            "Computer Architecture and Organization",
            "Integral Calculus",
            "Advanced Object Oriented Programming",
            "Introduction to Numerical Analysis",
            "Calculus-Based Physics",
            "Operating Systems",
            "Data Structures and Algorithms Analysis",
            "Probability and Statistics (w/ Lab)",
            "Networks and Communications",
            "Intelligent Agents",
            "Automata Theory and Formal Languages",
            "Software Engineering 1",
            "Chemistry for Engineers",
            "Modeling and Simulation",
            "Algorithms and Complexity",
            "Human Computer Interaction",
            "Information Assurance and Security",
            "Software Engineering 2",
            "Parallel and Distributed Computing"
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
                value=scale_value,
                command=self.check_button_state
            )
            radio_button.grid(row=3, column=scale_value, padx=5)

        next_button = tk.Button(self.root, text="Next Course", command=self.next_course)
        next_button.grid(row=4, column=2, pady=10)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_survey, state=tk.DISABLED)
        self.submit_button.grid(row=4, column=3, pady=10)

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
            self.submit_button.config(state=tk.NORMAL)  # Enable submit button at the last question

    def submit_survey(self):
        submitted_responses = [var.get() for var in self.responses]
        for response in submitted_responses:
            if self.current_course_idx < len(self.courses_it):
                self.counter_it += response
            else:
                self.counter_cs += response

        messagebox.showinfo("Survey Complete", f"Thank you for completing the survey!\n\nResults:\nBSIT Counter: {self.counter_it}\nBSCS Counter: {self.counter_cs}\n\nWe recommend you to take {'BSIT' if self.counter_it > self.counter_cs else 'BSCS'}.")

        self.root.destroy()

    def check_button_state(self):
        # Enable the submit button only when the user is at the last question
        if self.current_course_idx == len(self.courses_it) - 1:
            self.submit_button.config(state=tk.NORMAL)
        else:
            self.submit_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    survey_app = LikertScaleSurvey(root)
    root.mainloop()
