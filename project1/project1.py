# Movie Quotes Analysis Section
def is_question(text):
    # is user inputing a question? 
    if text[-1]== "?":
        return True
    else:
        print('I only respond to questions!')

def get_first_quotes(quotes):
    # get the first quote
    return [quote[0] for quote in quotes]

def get_first_questions(quotes):
    is_question= []
    for quote in quotes:
        first = quote[0]
        if is_question(first):
            is_question.append(first)
    return is_question

def count_question_quotes(quotes):
    return len(get_first_questions(quotes))
    # count the number of quotes that are questions
    