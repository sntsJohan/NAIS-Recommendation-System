import tkinter as tk
from tkinter import IntVar

class LikertScaleSurvey:
    def __init__(self, root):
        self.root = root
        self.root.title("Likert Scale Survey")

        self.courses = [
            "ITE 001 - Computer Programming 1",
            "MATH 013A - Linear Algebra",
            "MATH 006 - Discrete Mathematics",
            "ITE 012 - Computer Programming 2",
            "CS 201 - Data Structures and Algorithms",
            "IT 004 - Web Systems and Technologies",
            "IE 301B - Applied Statistics",
            "ITE 014 - Information Management",
            "IT 012 - Platform Technologies",
            "IT 005 - Integrative Programming and Technologies",
            "MATH 004 - Quantitative Methods (Including Modelling and Simulation)",
            "IT 006 - Networking 1",
            "IT 003 - Advanced Database Systems",
            "TECH 101 - Technopreneurship",
            "IT 009 - Systems Integration and Architecture 1",
            "IT 401 - Data Mining and Warehousing",
            "CS 409 - Mobile Computing",
            "IT 001 - Information Assurance and Security 1",
            "ITE 013 - Application Development and Emerging Technologies",
            "IT 007 - Networking 2",
            "ITE 030 - Data Analytics",
            "ITE 015 - Social and Professional Issues",
            "IT 008 - Systems and Administration Maintenance",
            "IT 002 - Information Assurance and Security 2",
            "ITE 010 - Systems Integration and Architecture 2",
            "ITE 503 - Current Trends and Issues in Computing",
            "IT 016 - Event Driven Programming",
            "IT 015 - Introduction to Game Development",
            "SAD 003 - System Analysis and Design",
            "IT 014 - Human Computer Interaction 2",
            "IT 011 - Integrative Programming Technologies 2",
            "IT 013 - Web Systems and Technologies 2",
            "CS 002 - Object Oriented Programming",
            "ITE 404 - Introduction to Data Science in Python",
            "SAP 501 - Business Analytics Using SAP Business Warehousing",
            "ITE 405 - Applied Plotting, Charting, and Data Representation",
            "ITE 406 - Applied Text Mining and Applied Social Network Analysis"
        ]

        self.current_course_idx = 0
        self.responses = []

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text=self.courses[self.current_course_idx], font=("Helvetica", 14), pady=10)
        self.label.grid(row=0, column=0, columnspan=6)

        likert_var = IntVar()
        likert_var.set(0)  # Default value

        likert_labels = ["Not at all", "Slightly", "Neutral", "Moderately", "Extremely"]

        for scale_value, label_text in enumerate(likert_labels, start=1):
            label = tk.Label(self.root, text=label_text, padx=5)
            label.grid(row=1, column=scale_value, sticky=tk.W)

        for scale_value in range(1, 6):
            radio_button = tk.Radiobutton(
                self.root,
                text=str(scale_value),
                variable=likert_var,
                value=scale_value
            )
            radio_button.grid(row=2, column=scale_value, padx=5)

        next_button = tk.Button(self.root, text="Next Course", command=self.next_course)
        next_button.grid(row=3, column=2, pady=10)

        submit_button = tk.Button(self.root, text="Submit", command=self.submit_survey)
        submit_button.grid(row=3, column=3, pady=10)

        self.responses.append(likert_var)

    def next_course(self):
        self.current_course_idx += 1
        if self.current_course_idx < len(self.courses):
            self.label.config(text=self.courses[self.current_course_idx])
        else:
            self.label.config(text="Survey complete")

    def submit_survey(self):
        submitted_responses = [var.get() for var in self.responses]
        print("Survey responses:", submitted_responses)
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    survey_app = LikertScaleSurvey(root)
    root.mainloop()
