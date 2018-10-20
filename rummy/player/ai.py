# -*- coding: utf-8 -*-
from random import choice

from player.player_actions import PlayerActions
from rummy.player.player import Player
from ui.view import View


class AI(Player):

    def show_turn_start(self):
        output = ''
        if self.ai_only:
            output += View.template_turn_start(self)
        else:
            output += View.template_ai_turn_start(self)
        output += View.template_ai_thought(self, 'Choosing pick up')
        return output

    def show_turn_end(self):
        output = ''
        if self.ai_only:
            output += View.template_ai_turn_end(self)
        output += View.template_ai_thought(self, 'Choosing card to discard')
        return output

    def choose_to_discard_or_pick_up(self):
        output = ''
        if self.round.deck.has_discard():
            current_score = self.hand.get_score()
            scores = self.melds.find_discard_scores(self.hand.get_hand(), self.round.deck.inspect_discard())
            if self.ai_only:
                output += View.template_ai_discard_data(current_score, scores)
            output += self.choose_pickup(current_score, scores)
        else:
            PlayerActions.take_from_deck(self.hand, self.round.deck)
            output += View.template_ai_thought(self, 'Drawing from deck')
        return output

    def choose_pickup(self, current_score, scores):
        output = ''
        if min(scores) < current_score - 4 or min(scores) <= 10:
            PlayerActions.take_from_discard(self.hand, self.round.deck)
            output += View.template_ai_thought(self, 'Drawing from discard')
        else:
            PlayerActions.take_from_deck(self.hand, self.round.deck)
            output += View.template_ai_thought(self, 'Drawing from deck')
        return output

    def discard_or_knock(self):
        scores = self.melds.find_discard_scores(self.hand.get_hand())
        score = min(scores)
        if score <= 10 and not self.round.knocked:
            self.round.knocked = True
        if scores.count(score) > 1:
            choices = [(i, x) for (i, x) in enumerate(scores) if (x == score)]
            discard = choice(choices)[0]
        else:
            discard = scores.index(score)
        discard = self.hand.discard_card(discard)
        self.round.deck.discard_card(discard)

        return self.show_discard()

    def show_discard(self):
        output = ''
        if self.ai_only:
            output += View.template_ai_hand_data(self.round.deck.inspect_discard(), self.hand.get_score())
        output += 'Discarded: %s' % self.round.deck.inspect_discard()
        return output
