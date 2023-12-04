import tkinter as tk
from tkinter import IntVar, messagebox
import random

class LikertScaleSurvey:
    def __init__(self, root):
        self.root = root
        self.root.title("Likert Scale Survey")

        self.courses_it = [
            {"course": "Introduction to Human Computer Interaction", "units": 6},
            {"course": "Web Systems and Technologies", "units": 3},
            {"course": "Modern Biology", "units": 3},
            {"course": "Applied Statistics", "units": 3},
            {"course": "Platform Technologies", "units": 3},
            {"course": "Integrative Programming and Technologies", "units": 3},
            {"course": "Networking", "units": 6},
            {"course": "Advanced Database Systems", "units": 3},
            {"course": "Systems Integration and Architecture", "units": 6},
            {"course": "Data Mining and Warehousing", "units": 3},
            {"course": "Information Assurance and Security 1", "units": 6},
            {"course": "Data Analytic", "units": 3},
            {"course": "Social and Professional Issues", "units": 3},
            {"course": "Systems Administration and Maintenance", "units": 3},
        ]

        self.courses_cs = [
            {"course": "Number Theory", "units": 3},
            {"course": "Symbolic Logic", "units": 3},
            {"course": "Differential Calculus", "units": 4},
            {"course": "Principles of Programming Languages", "units": 3},
            {"course": "Computer Architecture and Organization", "units": 3},
            {"course": "Integral Calculus", "units": 4},
            {"course": "Advanced Object-Oriented Programming", "units": 3},
            {"course": "Introduction to Numerical Analysis", "units": 3},
            {"course": "Calculus-Based Physics (Physics for Engineers)", "units": 4},
            {"course": "Operating Systems", "units": 3},
            {"course": "Probability and Statistics (w/ Lab)", "units": 3},
            {"course": "Networks and Communications", "units": 3},
            {"course": "Intelligent Agents", "units": 3},
            {"course": "Automata Theory and Formal Languages", "units": 3},
            {"course": "Software Engineering", "units": 6},
            {"course": "Algorithms and Complexity", "units": 3},
            {"course": "Human Computer Interaction", "units": 3},
            {"course": "Information Assurance and Security", "units": 3},
            {"course": "Parallel and Distributed Computing", "units": 3},
        ]

        self.general_cs = [
            "You enjoy solving complex mathematical and logical problems.",
            "Creating something new piques your interest.",
            "Exploring the mathematical foundations of computing, such as discrete mathematics and formal logic, appeals to you.",
            "Finding the most efficient solution to a programming challenge is a satisfying endeavor for you.",
            "Are you interested in the theoretical aspects of artificial intelligence and machine learning?",
            "Do you prefer a career path that involves more theoretical research and innovation?"
        ]

        self.general_it = [
            "You are interested in the creative aspects of designing user-friendly software interfaces.",
            "You see yourself applying existing technologies to solve real-world challenges.",
            "Ensuring the security and integrity of computer systems and networks is a priority for you.",
            "Managing and implementing technology solutions is more appealing to you than focusing on theoretical aspects like algorithms.",
            "You prefer hands-on, practical problem-solving related to technology and computer systems.",
            "You like web development more than system development."
        ]

        # Concatenate IT and CS courses, then shuffle
        all_courses = self.courses_it + self.courses_cs
        random.shuffle(all_courses)

        # Randomly select 10 courses from the concatenated list
        self.displayed_courses = random.sample(all_courses, 10)

        self.current_course_idx = 0
        self.responses = []
        self.counter_it = 0
        self.counter_cs = 0

        self.create_widgets()

    def create_widgets(self):
        intro_label = tk.Label(self.root, text="Please indicate how you feel about each course on a scale from 1 to 5, where 1 is 'Not at all' and 5 is 'Extremely'.", font=("Helvetica", 12), pady=10)
        intro_label.grid(row=0, column=0, columnspan=6)

        self.label = tk.Label(self.root, text=self.displayed_courses[self.current_course_idx]["course"], font=("Helvetica", 14), pady=10)
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
        next_button.grid(row=4, column=0, columnspan=6, pady=10)

        self.responses.append((likert_var, self.current_course_units()))

    def next_course(self):
        self.current_course_idx += 1
        if self.current_course_idx < 10:
            self.label.config(text=self.displayed_courses[self.current_course_idx]["course"])
        else:
            self.show_result()

    def show_result(self):
        submitted_responses = [var.get() for var, _ in self.responses]
        weights = [units for _, units in self.responses]

        for idx, (response, weight) in enumerate(zip(submitted_responses, weights)):
            if idx < 5:
                # Courses from the first five are IT courses
                self.counter_it += response * (17 / 18) * weight
            else:
                # Courses from the next five are CS courses
                self.counter_cs += response * weight

        messagebox.showinfo("Survey Complete", f"Thank you for completing the survey!\n\nResults:\nBSIT Counter: {self.counter_it}\nBSCS Counter: {self.counter_cs}\n\nWe recommend you to take {'BSIT' if self.counter_it > self.counter_cs else 'BSCS'}.")

        self.root.destroy()

    def check_button_state(self):
        # Enable the "Next Course" button only when the user is not at the last question
        if self.current_course_idx < 9:
            return
        self.next_course()

    def current_course_units(self):
        return self.displayed_courses[self.current_course_idx]["units"]

if __name__ == "__main__":
    root = tk.Tk()
    survey_app = LikertScaleSurvey(root)
    root.mainloop()
