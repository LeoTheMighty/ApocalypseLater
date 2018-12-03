import pygame


class Sprite(pygame.sprite.Sprite):
    def __init__(self, groups=[]):
        super().__init__(groups)

        # The state for the sprite
        self.state = "released"
        self.mouse_state = "released"

        # This makes sure that the rect actually exists
        # self.rect = self.rect

    def refresh(self):
        print("NOT IMPLEMENTED!!! (refresh) (for " + self.__class__.__name__ + ")")

    def refresh_sprite(self, action, mouse_pos):
        self.refresh()
        return_value = None
        if action == "press":
            self.mouse_state = "pressed"
        elif action == "release":
            self.mouse_state = "released"
        if self.screen_rect.collidepoint(mouse_pos):
            if action == "release":
                return_value = self.click()
            elif self.mouse_state == "pressed":
                self.state = "pushed"
                return_value = self.push()
            else:
                self.state = "highlighted"
                return_value = self.highlight()
        else:
            self.state = "released"
            return_value = self.release()

        # print(self.mouse_state)
        return return_value

    def push(self):
        print("NOT IMPLEMENTED!!! (release) (for " + self.__class__.__name__ + ")")
        return None

    def highlight(self):
        print("NOT IMPLEMENTED!!! (release) (for " + self.__class__.__name__ + ")")
        return None

    def release(self):
        print("NOT IMPLEMENTED!!! (release) (for " + self.__class__.__name__ + ")")
        return None

    def click(self):
        print("NOT IMPLEMENTED!!! (click) (for " + self.__class__.__name__ + ")")
        return None

