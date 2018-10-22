#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from time import sleep

import colorama

from rummy.game.round import Round
from rummy.game.score import Score
from rummy.game.setup_players import SetupPlayers
from rummy.player.human import Human
from rummy.ui.menu_action_dialog import MenuActionDialog
from rummy.ui.user_input import UserInput
from rummy.ui.view import View


class Play:
    def __init__(self):
        self.colorama()
        SetupPlayers.choose_players()
        self.players = SetupPlayers.create_players()
        self.ai_only = not any(isinstance(x, Human) for x in self.players)
        self.score = Score(self.players)
        self.round = Round(self.players)
        self.round.deal_cards(self.players)
        self.play_game()

    @staticmethod
    def colorama():
        if 'PYCHARM_HOSTED' in os.environ:
            convert = False  # in PyCharm, we should disable convert
            strip = False
        else:
            convert = None
            strip = None
        colorama.init(convert=convert, strip=strip)

    def play_game(self):
        while self.round.last_turn != len(self.players):
            self.round.prepare_turn()
            player = self.players[self.round.current_player]
            player.turn(self.round)
            self.round.end_turn()
        self.end_round()
        sleep(1.2)
        self.start_new_round_or_end_game()

    def start_new_round_or_end_game(self):
        if self.score.is_end_of_game():
            self.score.end_game()
        else:
            self.round.rotate_first_player()
            if not self.ai_only:
                self.confirm_start_new_round()
            self.round.prepare_new_round()
            self.round.deal_cards(self.players)
            self.play_game()

    def confirm_start_new_round(self):
        UserInput.create_input(MenuActionDialog.next_round())

    def end_round(self):
        self.score.update_player_scores()
        View.render(
            View.template_this_round_score(self.score.get_end_of_round_scores(), self.score.get_current_game_scores())
        )


# start game
if __name__ == "__main__":
    Play()
