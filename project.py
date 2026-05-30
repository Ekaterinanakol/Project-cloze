import re

def tokenize_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    return words
    
def display_text_with_gaps(quiz_text):
    formatted_text = " ".join(quiz_text)
    print("Текст с пропусками:")
    print(formatted_text)
    
def clean_tokens (formatted_text):
    answers = []
    for i in range(len(formatted_text)):
        if (i+1) == 10:
            answers += i
            formatted_text[i] = "___"
            task = " ".join(formatted_text)
    return task, answers
    
def get_answers(num_gaps):
    answers = []
    for i in range(num_gaps):
        answer = input(f"Ответ для пропуска {i+1}: ").strip()
        answers.append(answer)
    return answers
    
def calculate_correct_answers(user_answers, correct_answers):
    result = 0
    for answer in range(len(correct_answers)):
        if user_answers[answer] == correct_answers[answer]:
            result+=1
    return result

tokenize_file