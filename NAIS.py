import numpy as np
import spacy
from difflib import get_close_matches
from collections import Counter

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

# Keywords for Computer Science (CS) and Information Technology (IT) based on open-ended questions
# Keywords for Computer Science (CS) and Information Technology (IT) based on open-ended questions
cs_keywords = [
    "programming", "coding", "algorithms",
    "computer", "mathematics", "logic",
    "cryptography", "security", "hackathons",
    "software", "machine learning",
    "artificial intelligence", "data", "web",
    "database", "graphics", "vision",
    "language", "networking", "systems",
    "architecture", "robotics", "game",
    "virtual", "augmented", "scientific",
    "numerical", "big data", "internet",
    "blockchain", "quantum", "ethical",
    "digital", "technology", "volunteering",
    "coding", "language", "open-source",
    "bootcamps", "certifications", "mentorship",
    "workshops", "competitions", "biology",
    "design", "blogs", "social", "amogus1"
]

it_keywords = [
    "IT", "network", "systems",
    "database", "web", "cloud",
    "cybersecurity", "consulting",
    "business", "user", "human-computer",
    "mobile", "e-commerce", "project",
    "governance", "strategy", "technology",
    "integration", "service", "risk",
    "compliance", "data", "privacy",
    "digital", "IoT", "artificial",
    "blockchain", "augmented", "virtual",
    "health", "educational", "telecommunications",
    "wireless", "network", "ethical",
    "forensics", "ethics", "law",
    "social", "sustainability", "change",
    "healthcare", "finance", "education",
    "trends"
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
    for keyword in keyword_list:
        # Use spaCy's efficient matching capabilities
        matches = [token.text.lower() for token in doc if keyword.lower() in token.text.lower()]
        keyword_counts[keyword] = len(matches)

    return keyword_counts

open_ended_response = input("What experiences or activities have influenced your interest in the technological field?\n")
open_ended_response += input("How do you envision your career in the future?\n")

keywords_cs = analyze_open_ended_response(open_ended_response, cs_keywords)
keywords_it = analyze_open_ended_response(open_ended_response, it_keywords)

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


    if keywords_cs > keywords_it:
        print("Based on your open-ended responses, you seem more interested in Computer Science.")
        # You can adjust the recommendation logic accordingly
    elif keywords_cs < keywords_it:
        print("Based on your open-ended responses, you seem more interested in Information Technology.")
        # You can adjust the recommendation logic accordingly
    else:
        print("Based on your open-ended responses, your interests in Computer Science and Information Technology are equally strong.")
        # You can adjust the recommendation logic accordingly

    print(keywords_cs)
    print(keywords_it)
1
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

