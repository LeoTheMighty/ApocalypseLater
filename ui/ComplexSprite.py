import pygame


class ComplexSprite(pygame.sprite.Sprite):
    def __init__(self, groups=[]):
        super().__init__(groups)
        self.sprite_groups = []

    def add_sprite_group(self, group):
        self.sprite_groups.append(group)

