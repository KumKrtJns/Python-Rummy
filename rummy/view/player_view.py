from abc import abstractmethod

from rummy.text_template import TextTemplate
from rummy.constants import TEMPLATE_PATH


class PlayerView:

    @staticmethod
    @abstractmethod
    def turn_start(player):
        pass

    @staticmethod
    @abstractmethod
    def turn_end(player):
        pass

    @staticmethod
    @abstractmethod
    def discarded(discard):
        pass

    @staticmethod
    def knocked():
        return TextTemplate.render(
            TEMPLATE_PATH + '/knocked.txt'
        )
