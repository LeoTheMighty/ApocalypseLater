from .UIConstants import *
import pygame


class ScreenManager:
    def __init__(self, display, root_screen):
        # Init all of the screen stuff
        self.main_screen = display
        self.main_screen.convert_alpha()
        self.screen_root_node = ScreenNode(root_screen, None)
        self.current_screen = self.screen_root_node
        self.darken_screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()
        self.darken_screen.fill((0, 0, 0, 100))

    def refresh(self):
        if_continue = True
        events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if_continue = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if_continue = False
            else:
                events.append(event)

        return_value, next_screen_values = self.get_screen().refresh_screen(events)
        # Use some "previous screen logic" maybe?
        screen = self.get_screen()
        # Center the screen
        self.main_screen.blit(screen,
                              (int((SCREEN_WIDTH - screen.get_width()) / 2),
                               int((SCREEN_HEIGHT - screen.get_height()) / 2)))
        pygame.display.flip()

        if return_value is not None:
            if return_value == -1:
                self.previous_screen(next_screen_values)
            elif return_value == 42069:
                if_continue = False
            elif 0 <= return_value < len(self.current_screen.next_screens):
                self.next_screen(return_value, next_screen_values)
            else:
                print("PROBLEMATIC RETURN VALUE = " + str(return_value))
        return if_continue

    def get_screen(self):
        return self.current_screen.screen

    def add_screen_to_current(self, screen):
        return self.current_screen.add_screen(screen)

    def add_screen_node_to_current(self, screen_node):
        return self.current_screen.add_screen_node(screen_node)

    def next_screen(self, screen_index, next_screen_values):
        self.current_screen = self.current_screen.next_screen(screen_index)
        self.current_screen.screen.receive_next_values(next_screen_values)
        self.main_screen.blit(self.darken_screen, (0, 0))
        return self.get_screen()

    def previous_screen(self, next_screen_values):
        self.current_screen = self.current_screen.parent_screen
        self.current_screen.screen.receive_next_values(next_screen_values)
        return self.get_screen()

    def jump_to_root(self):
        self.current_screen = self.screen_root_node
        return self.get_screen()


class ScreenNode:
    def __init__(self, screen, parent_screen):
        self.screen = screen
        self.parent_screen = parent_screen
        self.next_screens = []

    def add_screen(self, screen):
        # index = len(self.next_screens)
        node = ScreenNode(screen, self)
        self.next_screens.append(node)
        return node

    def add_screen_node(self, screen_node):
        self.next_screens.append(screen_node)
        return screen_node

    def next_screen(self, screen_index):
        return self.next_screens[screen_index]
