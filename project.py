import re

def tokenize_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    return words

def clean_tokens(tokenized_text):
    answers = []
    gap_number = 1  # счетчик пропусков
    for i, word in enumerate(tokenized_text):
        if (i + 1) % 10 == 0:
            answers.append(word)
            tokenized_text[i] = f"{gap_number}.___"
            gap_number += 1
    task = " ".join(tokenized_text)
    return task, answers

def display_text_with_gaps(quiz_text):
    formatted_text = " ".join(quiz_text)
    print("Текст с пропусками:")
    print(formatted_text)

def get_answers(num_gaps):
    answers = []
    for i in range(num_gaps):
        answer = input(f"Ответ для пропуска {i + 1}: ").strip()
        answers.append(answer)
    return answers

def calculate_correct_answers(user_answers, correct_answers):
    if len(user_answers) != len(correct_answers):
        print("Количество ответов не совпадает")
    result = 0
    for i in range(min(len(correct_answers), len(user_answers))):
        if user_answers[i] == correct_answers[i]:
            result += 1
    return result

# вызовы функций
words = tokenize_file("humannature.txt")
words_with_gaps = words.copy()
task, correct = clean_tokens(words_with_gaps)
display_text_with_gaps(words_with_gaps)
user_answers = get_answers(len(correct))
score = calculate_correct_answers(user_answers, correct)
print(f"\nРезультат: {score}/{len(correct)}")