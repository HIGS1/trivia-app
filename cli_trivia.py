from utils import clear, input_int
import opentdb as trivia


def answer_question(question: trivia.Question, question_number: int = -1):
    clear()
    print(  # Using the "Ternary Operator" in python.
        f'{">> True or False" if question.question_type.value == "boolean" else ">> Multiple Choice"} Question ({question.difficulty.value}) [{question.category_name}]\n\n')

    # Display Answers
    print(f'Q{question_number if question_number > 0 else ""}: {question.statement}\n')
    for idx, answer in enumerate(question.possible_answers):
        print(f'{idx + 1} - {answer}')

    # Get the chosen answer
    given_answer = input_int(
        f'\n>> Type your answer (1 - {len(question.possible_answers)}): ', 1, len(question.possible_answers))

    # Check answer
    if question.possible_answers[given_answer - 1] == question.correct_answer:
        print(
            f'\nCorrect!\nThe answer is: {question.possible_answers[given_answer - 1]} ({given_answer})')
    else:
        print(
            f'\nUnlucky...\nThe Correct answer is: {question.correct_answer} ({question.possible_answers.index(question.correct_answer) + 1})\nGiven Answer: {question.possible_answers[given_answer - 1]} ({given_answer})')

    # Continue or Exit the program
    try:
        input('\n\nPress [Enter] to continue or [CRL + C] to Exit...')
    except KeyboardInterrupt:
        exit(0)

    # Clear the terminal
    clear()


def choose_category() -> trivia.QuestionCategory | None:
    clear()
    try:
        random_category = input('Random Category? (y/n): ')
    except:
        print('Closing Program.')
        exit(0)

    if random_category.strip().lower() == 'y' or random_category == 'yes':
        return None

    available_categories = trivia.QuestionCategory.get_categories()

    for idx, category in enumerate(available_categories):
        print(f'{idx + 1}) - {category.category_name}')

    chosen_category = input_int(
        f'\nSelect Category (1-{len(available_categories)}): ', 0, len(available_categories))

    return available_categories[chosen_category - 1]


def choose_difficulty() -> trivia.QuestionDifficulty | None:
    clear()
    try:
        random_difficulty = input('Random Difficulty? (y/n): ')
    except:
        print('Closing Program.')
        exit(0)

    if random_difficulty.strip().lower() == 'y' or random_difficulty == 'yes':
        return None

    available_difficulties = [
        diff for diff in trivia.QuestionDifficulty if diff.value != '']

    for idx, difficulty in enumerate(available_difficulties):
        print(f'{idx + 1}) - {difficulty.value.capitalize()}')

    chosen_difficulty = input_int(
        f'\nSelect Category (1-{len(available_difficulties)}): ', 0, len(available_difficulties))

    return available_difficulties[chosen_difficulty - 1]


def choose_question_type() -> trivia.QuestionType | None:
    clear()
    try:
        random_type = input('Random Question Type? (y/n): ')
    except:
        print('Closing Program.')
        exit(0)

    if random_type.strip().lower() == 'y' or random_type == 'yes':
        return None

    available_types = [
        t for t in trivia.QuestionType if t.value != '']

    for idx, q_type in enumerate(available_types):
        print(f'{idx + 1}) - {q_type.value.capitalize()}')

    chosen_type = input_int(
        f'\nSelect Category (1-{len(available_types)}): ', 0, len(available_types))

    return available_types[chosen_type - 1]


def main():
    category = choose_category()
    difficulty = choose_difficulty()
    question_type = choose_question_type()

    t = trivia.Trivia(
        input_int('Questions Amount (min 1 - max 50): ', 1, 50),
        category if category is not None else trivia.QuestionCategory.ANY,
        difficulty if difficulty is not None else trivia.QuestionDifficulty.ANY,
        question_type if question_type is not None else trivia.QuestionType.ANY,
    )
    questions = t.get_questions()

    for i, question in enumerate(questions):
        answer_question(question, i + 1)


if __name__ == "__main__":
    main()
