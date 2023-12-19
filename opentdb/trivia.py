from .trivia_errors import NoResusltsFoundError, RateLimitExceededError, InvalidParameterValueError
from .question_difficulty import QuestionDifficulty
from .question_category import QuestionCategory
from .question_type import QuestionType
from .question import Question
import requests
import json


class Trivia:
    _API_URL = 'https://opentdb.com/api.php'

    def __init__(self, questions: int, category: QuestionCategory, difficulty: QuestionDifficulty, question_type: QuestionType) -> None:
        '''
        Trivia Class Constructor

                Parameters:
                        questions (int): The Amount of questions the trivia should have (Min 1, Max is 50).
                        category (QuestionCategory): The Category of the questions the trivia should have.
                        difficulty (QuestionDifficulty): The Difficulty of the questions.
                        question_type (QuestionType): The Type of the questions (Either Multiple Choice or True/False).

                Returns:
                        Instance of (Trivia)
        '''
        self.question_amount = questions
        self.category = category
        self.difficulty = difficulty
        self.questions_type = question_type

    def get_questions(self) -> list[Question]:
        query_params = {'encode': 'base64'}
        # Amount of questions
        if self.question_amount <= 0 or self.question_amount > 50:
            raise ValueError(
                f'The Amount of Questions {self.question_amount} is wrong')
        else:
            query_params.update({'amount': self.question_amount})

        # Optional Params
        if self.category != '':
            query_params.update({'category': self.category.category_id})
        if self.difficulty != '':
            query_params.update({'difficulty': self.difficulty.value})
        if self.questions_type != '':
            query_params.update({'type': self.questions_type.value})

        # Send the GET Request
        response = requests.get(self._API_URL, query_params)

        # Deserialize the JSON data
        json_response: dict = json.loads(response.text)

        # Check the Response Code
        response_code: int = json_response.get('response_code')
        match response_code:
            case 0:
                pass
            case 1:
                raise NoResusltsFoundError(
                    'Could not return results. The API doesn\'t have enough questions for your query. (Ex. Asking for 50 Questions in a Category that only has 20.)')
            case 2:
                raise InvalidParameterValueError(
                    'Contains an invalid parameter. Arguements passed in aren\'t valid. (Ex. Amount = Five)')
            case 5:
                raise RateLimitExceededError(
                    'Too many requests have occurred. Each IP can only access the API once every 5 seconds.')
            case _:
                print(response_code)

        # Get all JSON Questions
        json_questions: list[dict[str, object]] = json_response.get('results')
        # print(json_questions)

        # Question Objects
        questions: list[Question] = []
        for json_q in json_questions:
            questions.append(
                Question.fromJSON(json_q)
            )
        
        # print(questions)
        return questions
