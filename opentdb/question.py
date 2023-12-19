from .question_difficulty import QuestionDifficulty
from .question_category import QuestionCategory
from .question_type import QuestionType
from base64 import b64decode


class Question:
    def __init__(
        self,
        statement: str,
        category_name: str,
        type: QuestionType,
        difficulty: QuestionDifficulty,
        correct_answer: str,
        incorrect_answers: list[str],
    ) -> None:
        self.statement = statement
        self.category_name = category_name
        self.question_type = type
        self.difficulty = difficulty
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers

        self.possible_answers: list[str] = [
            *self.incorrect_answers, self.correct_answer]
        self.possible_answers.sort()

    @staticmethod
    def fromJSON(json: dict):
        raw_answers = json['incorrect_answers']
        answers = []
        for answer in raw_answers:
            answers.append(b64decode(answer).decode('utf-8'))

        return Question(
            statement=b64decode(json['question']).decode('utf-8'),
            incorrect_answers=answers,
            correct_answer=b64decode(
                json['correct_answer']).decode('utf-8'),
            category_name=b64decode(json['category']).decode('utf-8'),
            difficulty=QuestionDifficulty(
                b64decode(json['difficulty']).decode('utf-8')),
            type=QuestionType(
                b64decode(json['type']).decode('utf-8')),
        )

    def __str__(self) -> str:
        return f'{self.statement} ({self.difficulty.value}) [{self.category_name}]\n{self.possible_answers}\n>>{self.correct_answer}'
