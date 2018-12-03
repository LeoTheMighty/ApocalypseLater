import pygame
from .Image import get_centered_rect
from ..Sprite import Sprite
from ..UIConstants import *


class Textbox(Sprite):
    def __init__(self, text, rect, font_size, screen_size=(SCREEN_WIDTH, SCREEN_HEIGHT), color=(0, 0, 0), font=None, centered=False, bold=False, italics=False):
        super().__init__()
        _, _, width, height = rect
        self.image = create_text_box(text, font_size, width, height, color, font, centered, bold, italics)
        # print(rect)
        self.rect, self.screen_rect = get_centered_rect(rect, screen_size)
        # print(self.rect)

    def refresh(self):
        return

    def release(self):
        return None

    def highlight(self):
        return None

    def push(self):
        return None

    def click(self):
        return None


def create_text_box(text, font_size, width, height, color, font, centered, bold, italics):
    # How to compile all the text together? Aka how to insert a new-line?
    if font is None:
        font = pygame.font.SysFont('Comic Sans MS', font_size, bold, italics)

    # TODO How do I make the final surface see-through, but not the ones I blot on top of it?
    final_surface = pygame.Surface((width, height)).convert_alpha()
    final_surface.fill((0, 0, 0, 0))
    # final_surface.set_alpha(0)
    x, y = (0, 0)

    # TODO Put words in one at a time until they overflow the line
    words = text.split(" ")

    current_line = ""
    previous_line = ""
    previous_line_surface = None
    i = len(words)
    for word in words:
        # Put it into the current line and render a new
        if current_line != "":
            current_line += " "
        current_line += word
        line_surface = font.render(current_line, True, color)
        if line_surface.get_width() > width:
            if previous_line_surface is not None:
                # Put in the previous line into the final surface
                place_x = x
                if centered:
                    place_x = int((width - previous_line_surface.get_width()) / 2)
                final_surface.blit(previous_line_surface.convert_alpha(), (place_x, y))
                y += (3 * previous_line_surface.get_height() / 4)
                previous_line_surface = None
                current_line = word
            else:
                # Put in the current line into the final surface
                place_x = x
                if centered:
                    place_x = int((width - line_surface.get_width()) / 2)
                final_surface.blit(line_surface.convert_alpha(), (place_x, y))
                y += (3 * line_surface.get_height() / 4)
                previous_line_surface = None
                current_line = ""
        else:
            previous_line_surface = line_surface

        # If this is the last thing
        if i == 1 and current_line != "":
            line_surface = font.render(current_line, True, color)
            place_x = x
            if centered:
                place_x = int((width - line_surface.get_width()) / 2)
            final_surface.blit(line_surface.convert_alpha(), (place_x, y))

        i -= 1

    return final_surface
