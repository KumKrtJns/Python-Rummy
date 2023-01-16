# -*- coding: utf-8 -*-

from player import AI
from player import Human
from ui import MenuActionDialog
from ui import UserInput


class Players:
    def __init__(self):
        self.players = []
        self.number_of_players = -1
        self.number_of_opponents = -1

    def choose_players(self):
        self.number_of_players = int(UserInput.create_input(MenuActionDialog.human_players()))
        for _ in range(int(self.number_of_players)):
            self.players.append(Human(len(self.players) + 1))

    def choose_opponents(self):
        if self.number_of_players in [-1, 0, 1]:
            self.number_of_opponents = int(
                UserInput.create_input(MenuActionDialog.ai_players(self.number_of_players)))
            ai_only = self.is_ai_only()
            for _ in range(int(self.number_of_opponents)):
                self.players.append(AI(len(self.players) + 1, ai_only))

    def is_ai_only(self):
        return True if self.number_of_players == 0 else False

    def get_players(self):
        return self.players
