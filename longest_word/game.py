# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import random
import string
import requests


class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        # [...]

        return self.__check_dictionary(word)


    @staticmethod
    def __check_dictionary(word):
        response = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        json_response = response.json()
        return json_response['found']
game = Game()
new_game = Game()
new_game.grid = list('KWIENFUQW')
print(new_game.is_valid('tomato'))
