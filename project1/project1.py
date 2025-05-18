import random
from project1_quotes import get_quotes
import string

quotes = get_quotes()
# Movie Quotes Analysis Section
def is_question(text):
    # is user inputing a question? 
    if text[-1] == "?":
        return True
    return False

def get_first_quotes(quotes):
    # get the first quote
    return [quote[0] for quote in quotes]

def get_first_questions(quotes):
    question_list = []
    for quote in quotes:
        first = quote[0]
        if is_question(first):
            question_list.append(first)
    return question_list

def count_question_quotes(quotes):
    return len(get_first_questions(quotes))
    # count the number of quotes that are questions

def  get_average_question_length(quotes):
    # get the average length of the questions
    qus_quotes = get_first_questions(quotes)
    total = 0
    for i in qus_quotes:
        total += len(i)
    sum = total / len(qus_quotes)
    return sum


def get_responses(quote,text):
    return_list = []
    for q,a in quote:
        if q == text:
            return_list.append(a)
    return return_list

def get_random_from_list(input_list):
    return random.choice(input_list)

def respond(quote, text):
    if not is_question(text):
        return "I only respond to questions!"
    
    responses = get_responses(quote, text)
    if responses:
        return get_random_from_list(responses)
    else:
        return "I don't know."


#Jaccard similarity
def lettersonly(text):
    clean_text = ""
    for char in text.lower():
        if char.isalpha() or char.isspace():
            clean_text += char
    return clean_text

def jaccard_similarity(text1, text2):   
    text1 = lettersonly(text1)
    text2 = lettersonly(text2)
    set1 = set(text1.split())
    set2 = set(text2.split())
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    if union == 0:
        return 0.0
    return intersection / union

#chatbot
def chatbot(version):
    print("Welcome!")
    while True:
        msg = input("Ask me anything. When you're done, just type 'bye'\n")
        msg_low = msg.lower()
        
        if msg_low == 'bye':
            print("Goodbye!")
            break
            
        if not is_question(msg):
            print("I only respond to questions!")
            continue
            
        answers = []
        
        if version == 0: 
            for q, a in quotes:
                if q.lower() == msg.lower():
                    answers.append(a)
                    
        elif version == 1:
            for q, a in quotes:
                if jaccard_similarity(q, msg) >= 0.6:
                    answers.append(a)
                    
        else:
            max_sim = 0
            for q, a in quotes:
                sim = jaccard_similarity(q, msg)
                if sim >= 0.6:
                    if sim > max_sim:
                        max_sim = sim
                        answers = [a]
                    elif sim == max_sim:
                        answers.append(a)
                    
        if answers:
            print(get_random_from_list(answers))
        else:
            print("I don't know.")

if __name__ == "__main__":
    chatbot(2)



