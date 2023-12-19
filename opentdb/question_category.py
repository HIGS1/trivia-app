import requests
import json


class QuestionCategory:
    ANY = ''

    def __init__(self, category_id: int, category_name: str) -> None:
        self.category_id = category_id
        self.category_name = category_name

    def __str__(self) -> str:
        return f'{self.category_id} - {self.category_name}'

    @staticmethod
    def fromJSON(json: dict):
        # print(json)
        try:
            return QuestionCategory(json.get('id'), json.get('name'))
        except:
            # print(f'WTF IS THIS? >> {json}')
            return None

    @staticmethod
    def get_categories():
        response = requests.get('https://opentdb.com/api_category.php')

        response_obj: dict = json.loads(response.text)

        json_categories = response_obj.get('trivia_categories')

        categories: list[QuestionCategory] = []
        for i, json_category in enumerate(json_categories):
            # print(f'HELLO {i + 1}: {json_category}')
            category = QuestionCategory.fromJSON(json_category)
            # print(category)
            if category is not None:
                categories.append(category)

        # print(categories)
        return categories
