from ..Sprite import Sprite
import pygame
from ..UIConstants import *
from .Image import get_centered_rect
from ..logic.Timer import Timer
import os


class NewsPrompt(Sprite):
    def __init__(self, identifier, color, rect, font=None, screen_size=(SCREEN_WIDTH, SCREEN_HEIGHT)):
        super().__init__()
        self.identifier = identifier
        self.color = color
        _, _, self.width, self.height = rect
        self.border_length = self.height / 8
        self.news_speed = 1

        self.font = None
        if font is None:
            self.font = pygame.font.Font(os.path.join("fonts", "OpenSans-Semibold.ttf"), 20)
            # self.font = pygame.font.SysFont("Times New Roman", int(self.width / 8.5), False, False)
        else:
            self.font = font

        self.rect, self.screen_rect = get_centered_rect(rect, screen_size)

        # Create the bar
        self.image = None
        self.set_background_bar()

        self.current_event = None
        self.event_text_surface = None
        self.event_timer = None

    def refresh(self):
        if self.event_timer is not None and self.event_text_surface is not None and self.current_event is not None:
            # Then show the event
            if not self.event_timer.has_finished():
                amount_done = self.event_timer.amount_done()
                start_x = self.width
                end_x = -self.event_text_surface.get_width()
                x = ((end_x - start_x) * amount_done) + start_x
                self.set_background_bar()
                self.image.blit(self.event_text_surface, (x, self.border_length))
                # pygame.draw.rect(self.image, )
            else:
                self.current_event = None
                self.event_timer = None
                self.set_background_bar()

    def set_background_bar(self):
        self.image = pygame.Surface((int(self.width), int(self.height)))
        self.image.fill((0, 0, 0))
        bar_width = self.width - (2 * self.border_length)
        bar_height = self.height - (2 * self.border_length)
        pygame.draw.rect(self.image, (255, 255, 255), (int(self.border_length), int(self.border_length), int(bar_width), int(bar_height)))
        self.image = self.image.convert_alpha()

    def show_event(self, event):
        if event is not None:
            # print("Setting news prompt feed to " + event.title)
            self.current_event = event
            # self.event_text_surface = pygame.Surface((self.width - (2 * self.border_length), self.height - (2 * self.border_length))).convert_alpha()
            # self.event_text_surface.fill((0, 0, 0, 0))

            # self.font = pygame.font.SysFont("Times New Roman", int(self.width / 10), False, False)
            self.event_text_surface = self.font.render(event.title, True, (0, 0, 0)).convert_alpha()
            self.event_timer = Timer(EVENT_TIME * self.event_text_surface.get_width() / 250 / self.news_speed)

    def change_speed(self, speed):
        if speed == "slow":
            self.news_speed = 1
        elif speed == "regular":
            self.news_speed = 1.5
        elif speed == "fast":
            self.news_speed = 2
        elif speed == "fastest":
            self.news_speed = 5
        else:
            print("Unrecognized speed = " + speed)

    def is_showing_event(self):
        return self.current_event is not None

    def push(self):
        return None

    def highlight(self):
        return None

    def release(self):
        return None

    def click(self):
        return self.identifier
