import random
from project1_quotes import get_quotes
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



#chatbot

def chatbot(version):
 if version == 0:
    print("Welcome!")
    while True:
        usr_in = input("Ask me anything. When you’re done, just type 'bye'\n")
        low_usrin = usr_in.lower()
        if low_usrin == 'bye':
            print("Goodbye!")
            break
        else:
            print(respond(quotes, usr_in))
if __name__ == "__main__":
    chatbot(0)
