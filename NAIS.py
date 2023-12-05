import numpy as np
import spacy
from difflib import get_close_matches
from collections import Counter

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

# Keywords for Computer Science (CS) and Information Technology (IT) based on open-ended questions
cs_keywords = [
    "programming projects", "coding challenges", "algorithmic problem-solving",
    "computer science courses", "mathematics courses", "logic puzzles", 
    "cryptography challenges", "security workshops", "hackathons", 
    "software development internships", "machine learning projects", 
    "artificial intelligence courses", "data science experiences", 
    "web development projects", "database management projects", 
    "computer graphics exploration", "computer vision experiments", 
    "natural language processing projects", "networking projects", 
    "operating systems exploration", "computer architecture studies", 
    "robotics projects", "game development experiences", 
    "virtual reality experiments", "augmented reality projects", 
    "scientific computing endeavors", "numerical analysis projects", 
    "big data exploration", "internet of things (IoT) experiments", 
    "blockchain projects", "quantum computing studies", 
    "ethical hacking experiences", "digital forensics projects", 
    "computer ethics exploration", "technology-related volunteering", 
    "participation in coding communities", "programming language exploration", 
    "contributions to open-source projects", "coding bootcamps", 
    "technology-related certifications", "mentorship in computer science", 
    "technology-related workshops", "coding competitions", 
    "research in computational biology", "computer-assisted design projects", 
    "technology-related blogs", "social network analysis projects" ,"amogus1"
]

it_keywords = [
    "IT infrastructure management", "network administration experiences", 
    "systems analysis projects", "database management experiences", 
    "web development for career goals", "cloud computing projects", 
    "cybersecurity experiences", "IT consulting experiences", 
    "business analysis in IT", "user experience improvement projects", 
    "human-computer interaction studies", "mobile app development for career", 
    "e-commerce technology exploration", "IT project management experiences", 
    "IT governance understanding", "IT strategy planning", 
    "technology integration projects", "IT service management experiences", 
    "IT risk management projects", "IT compliance understanding", 
    "data governance experiences", "data privacy awareness", 
    "digital transformation experiences", "IoT projects for career goals", 
    "artificial intelligence applications in IT", "blockchain in IT experiences", 
    "augmented reality in IT projects", "virtual reality in IT experiences", 
    "health IT projects", "educational technology exploration", 
    "telecommunications experiences", "wireless technologies exploration", 
    "network security projects", "ethical hacking in IT experiences", 
    "digital forensics in IT projects", "IT ethics understanding", 
    "IT law awareness", "social implications of IT understanding", 
    "IT for sustainability projects", "IT for social change projects", 
    "IT in healthcare projects", "IT in finance projects", 
    "IT in education projects", "future technology trends awareness",
]

# Program Title
print("---=========[NAIS Recommendation System]=========---\n")

def likert_scale_input(question):
    likert_scale = {
        '1': 'Not Interested at All',
        '2': 'Slightly Interested',
        '3': 'Moderately Interested',
        '4': 'Very Interested',
        '5': 'Extremely Interested'
    }

    print(question)
    for key, value in likert_scale.items():
        print(f'[{key}] {value}')

    while True:
        response = input('Choose a number (1-5): ')
        if response in likert_scale:
            return int(response)
        else:
            print('Invalid input. Please choose a number between 1 and 5.')


def analyze_open_ended_response(response, keyword_list):
    # Use NLP to extract keywords or topics from the open-ended response
    doc = nlp(response.lower())  # Convert to lowercase

    # Initialize a Counter to store counts for each keyword
    keyword_counts = Counter()

    # Count occurrences of each keyword in the response
    for token in doc:
        for keyword in keyword_list:
            if keyword in token.text.lower():
                keyword_counts[keyword] += 1

    return keyword_counts
    
open_ended_response_cs = input("What experiences or activities have influenced your interest in the technological field?\n")
open_ended_response_it = input("How do you envision your career in the future?\n")

keywords_cs = analyze_open_ended_response(open_ended_response_cs, cs_keywords)
keywords_it = analyze_open_ended_response(open_ended_response_it, it_keywords)

def compute_recommendation(cs_responses, it_responses):
    mean_cs = np.mean(cs_responses)
    mean_it = np.mean(it_responses)
    variance_cs = np.var(cs_responses, ddof=0)
    variance_it = np.var(it_responses, ddof=0)
    z_score = (mean_cs - mean_it) / np.sqrt((variance_cs / len(cs_responses)) + (variance_it / len(it_responses)))

    print(f"\nZ-Score: {z_score}")
    print(f"Mean for Computer Science: {mean_cs}")
    print(f"Mean for Information Technology: {mean_it}")
    print(f"Variance for Computer Science: {variance_cs}")
    print(f"Variance for Information Technology: {variance_it}")

    if abs(z_score) > 1.96:
        if mean_cs > mean_it:
            print("Reject null hypothesis. Recommended course: Computer Science (CS).")
        else:
            print("Reject null hypothesis. Recommended course: Information Technology (IT).")
    else:
        print("Accept null hypothesis. No strong recommendation.")

    count_cs = sum(keywords_cs.values())
    count_it = sum(keywords_it.values())

    print(count_cs)
    print(count_it)

    if count_cs > count_it:
        print("Based on your open-ended responses, you seem more interested in Computer Science.")
        # You can adjust the recommendation logic accordingly
    elif count_cs < count_it:
        print("Based on your open-ended responses, you seem more interested in Information Technology.")
        # You can adjust the recommendation logic accordingly
    else:
        print("Based on your open-ended responses, your interests in Computer Science and Information Technology are equally strong.")
        # You can adjust the recommendation logic accordingly

# Collect responses for Computer Science (CS) and Information Technology (IT) questions
cs_responses = [
    likert_scale_input("\nRelationships between different kinds of numbers such as natural numbers and integers."),
    likert_scale_input("\nMathematics applied in cryptography, device authentication, and security systems."),
    likert_scale_input("\nSolving complex mathematical and logical problems.")
]

it_responses = [
    likert_scale_input("\nDesigning and evaluating computer systems and technologies that people interact with."),
    likert_scale_input("\nCreating user-friendly and interactive human computer interfaces."),
    likert_scale_input("\nApplying existing technologies to solve real-world challenges.")
]

# Compute recommendation
compute_recommendation(cs_responses, it_responses)
