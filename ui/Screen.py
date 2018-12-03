from .UIConstants import *
import pygame
from .aspects.Image import create_image


class Screen(pygame.Surface):
    def __init__(self, image_path, width=SCREEN_WIDTH, height=SCREEN_HEIGHT):
        super().__init__((width, height), pygame.SRCALPHA)
        #self = self.convert_alpha()
        # self.fill((255, 255, 255, 0))
        # self.background_image = pygame.image.load(image_path)
        # self.background_image = pygame.transform.scale(self.background_image, (width, height))
        self.background_image = create_image(width, height, image_path).convert_alpha()
        self.sprite_groups = []

    def add_sprite_group(self, sprite_group):
        self.sprite_groups.append(sprite_group)

    def add_to_sprite_group(self, sprite, index):
        self.sprite_groups[index].add(sprite)

    def refresh(self):
        return None, None
        # print("NOT IMPLEMENTED FOR THIS CLASS")

    def refresh_screen(self, events):
        # return_vaI#lue = None
        # next_screen_values = None
        mouse_pos = pygame.mouse.get_pos()
        action = None
        return_value, next_screen_values = self.refresh()
        if return_value is None:
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    action = "press"
                    # centered_pos = (mouse_pos[0] - self.get_width() / 2) / self.get_width(), (mouse_pos[1] - self.get_height() / 2) / self.get_height()
                    # print(centered_pos)
                elif event.type == pygame.MOUSEBUTTONUP:
                    action = "release"
            self.blit(self.background_image, (0, 0))
            for group in self.sprite_groups:
                for sprite in group.sprites():
                    identifier = sprite.refresh_sprite(action, mouse_pos)
                    if identifier is not None:
                        _return_value, _next_screen_values = self.action(identifier)
                        if _return_value is not None:
                            return_value = _return_value
                            next_screen_values = _next_screen_values
                group.draw(self)
        return return_value, next_screen_values

    def action(self, identifier):
        print("NOT IMPLEMENTED FOR THIS CLASS")
        return None, None

    # Next values should be a dictionary of all the values to pass on
    def receive_next_values(self, next_values):
        print("NOT IMPLEMENTED FOR THIS CLASS")


