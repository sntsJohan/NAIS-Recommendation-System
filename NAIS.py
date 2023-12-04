import tkinter as tk
from tkinter import IntVar, messagebox
import random

class LikertScaleSurvey:
    def __init__(self, root):
        self.root = root
        self.root.title("Likert Scale Survey")
        self.current_stage = "Courses"
        self.current_question_idx = 0

        self.courses_it = [
            {"course": "Introduction to Human Computer Interaction"},
            {"course": "Web Systems and Technologies"},
            {"course": "Modern Biology"},
            {"course": "Applied Statistics"},
            {"course": "Platform Technologies"},
            {"course": "Integrative Programming and Technologies"},
            {"course": "Networking"},
            {"course": "Advanced Database Systems"},
            {"course": "Systems Integration and Architecture"},
            {"course": "Data Mining and Warehousing"},
            {"course": "Information Assurance and Security 1"},
            {"course": "Data Analytic"},
            {"course": "Social and Professional Issues"},
            {"course": "Systems Administration and Maintenance"},
        ]

        self.courses_cs = [
            {"course": "Number Theory"},
            {"course": "Symbolic Logic"},
            {"course": "Differential Calculus"},
            {"course": "Principles of Programming Languages"},
            {"course": "Computer Architecture and Organization"},
            {"course": "Integral Calculus"},
            {"course": "Advanced Object-Oriented Programming"},
            {"course": "Introduction to Numerical Analysis"},
            {"course": "Calculus-Based Physics (Physics for Engineers)"},
            {"course": "Operating Systems"},
            {"course": "Probability and Statistics (w/ Lab)"},
            {"course": "Networks and Communications"},
            {"course": "Intelligent Agents"},
            {"course": "Automata Theory and Formal Languages"},
            {"course": "Software Engineering"},
            {"course": "Algorithms and Complexity"},
            {"course": "Human Computer Interaction"},
            {"course": "Information Assurance and Security"},
            {"course": "Parallel and Distributed Computing"},
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

        self.job_roles_cs = [
            "Artificial Intelligence Engineer",
            "Back-end Engineer",
            "Computer Scientist",
            "Data Scientist",
            "Full Stack Developer",
            "Information Security Analyst",
            "Robotics Engineer",
            "Software Developer",
            "Software Engineer",
            "Web Developer"
        ]

        self.job_roles_it = [
            "Computer Technician",
            "Cybersecurity Specialist",
            "Database Administrator",
            "Helpdesk Technician",
            "IT Consultant",
            "IT Project Manager",
            "Network Administrator",
            "Network Engineer",
            "System Administrator",
            "Technical Support Specialist"
        ]

        self.openendedquestions = [
            "What experiences or activities have influenced your interest in the technological field?",
            "How do you envision your career in the future?"
        ]

        # Likert scale labels for job role questions
        likert_labels_job_roles = ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]

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

        next_button = tk.Button(self.root, text="Next", command=self.next_stage)
        next_button.grid(row=4, column=0, columnspan=6, pady=10)

        self.responses.append((likert_var, self.current_course_category()))

    def next_stage(self):
        if self.current_stage == "Courses":
            if self.current_course_idx < 9:
                self.current_course_idx += 1
                self.label.config(text=self.displayed_courses[self.current_course_idx]["course"])
            elif self.current_course_idx == 9:
                self.current_stage = "General"
                self.current_question_idx = 0
                self.label.config(text=self.general_it[self.current_question_idx])
        elif self.current_stage == "General":
            if self.current_question_idx < len(self.general_it) - 1:
                self.current_question_idx += 1
                self.label.config(text=self.general_it[self.current_question_idx])
            elif self.current_question_idx == len(self.general_it) - 1:
                self.current_stage = "Job Roles"
                self.current_question_idx = 0
                self.label.config(text=self.job_roles_it[self.current_question_idx])
        elif self.current_stage == "Job Roles":
            if self.current_question_idx < len(self.job_roles_it) - 1:
                self.current_question_idx += 1
                self.label.config(text=self.job_roles_it[self.current_question_idx])
            elif self.current_question_idx == len(self.job_roles_it) - 1:
                self.current_stage = "Open Ended"
                self.current_question_idx = 0
                self.label.config(text=self.openendedquestions[self.current_question_idx])
        elif self.current_stage == "Open Ended":
            if self.current_question_idx < len(self.openendedquestions) - 1:
                self.current_question_idx += 1
                self.label.config(text=self.openendedquestions[self.current_question_idx])
            elif self.current_question_idx == len(self.openendedquestions) - 1:
                self.show_result()

    def show_result(self):
        submitted_responses = [var.get() for var, _ in self.responses]
        # (unchanged code)

        messagebox.showinfo("Survey Complete", f"Thank you for completing the survey!\n\nResults:\nBSIT Counter: {self.counter_it}\nBSCS Counter: {self.counter_cs}\n\nWe recommend you to take {'BSIT' if self.counter_it > self.counter_cs else 'BSCS'}.")

        self.root.destroy()

    def check_button_state(self):
        # Enable the "Next Course" button only when the user is not at the last question
        if self.current_course_idx < 9:
            return
        self.next_stage()

    def current_course_category(self):
        return "IT" if self.displayed_courses[self.current_course_idx] in self.courses_it else "CS"

if __name__ == "__main__":
    root = tk.Tk()
    survey_app = LikertScaleSurvey(root)
    root.mainloop()
