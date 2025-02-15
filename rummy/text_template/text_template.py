# coding=utf-8
import os
from string import Template
from rummy.ansi_colours import Colour


class TextTemplate(Colour):

    @classmethod
    def render(cls, template, **kwargs):
        if not os.path.isfile(template):
            raise OSError("Template was not found: " + template)
        with open(template, 'r') as content_file:
            content = content_file.read()
            t = Template(content)
            kwargs.update(Colour.colours)
            return t.substitute(**kwargs)

if __name__ == "__main__":
    from rummy.constants import TEMPLATE_PATH
    print(TextTemplate.render(TEMPLATE_PATH + '/knocked.txt'))
    #${red}A Player has knocked, this is your last turn!!!${colour_end}