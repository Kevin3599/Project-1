#yongcheng Zhao project 1
from project1_quotes import get_quotes, get_practice_quotes
def is_question():
    usr_input = input()
    if usr_input[-1] == '?':
        return True
    else:
        return False
    
def get_fisrt_quaote():
    quotes_list = input("Enter a list of quotes: ")
    first_quotes = []    
    for quote_pair in quotes_list:
        first_quotes.append(quote_pair[0])
    return first_quotes

def get_first_questions(quotes_list):
    return [q[0] for q in quotes_list if q[0].strip()[-1] == '?']

def count_questions_quotes(quotes_list):
    