import pygame
from ui.screens.MainMenu import MainMenu
from ui.screens.GameScreen import GameScreen
from ui.screens.LoadGameScreen import LoadGameScreen
from ui.screens.CreditsScreen import CreditsScreen
from ui.logic.GameHandler import GameHandler
from ui.screens.PlacePopup import PlacePopup
from ui.screens.MoneyPopup import MoneyPopup
from ui.screens.ClosenessProgressBarsPopup import ClosenessProgressBarsPopup
from ui.screens.ForceProgressBarsPopup import ForceProgressBarsPopup
from ui.screens.SettingsPopup import SettingsPopup
from ui.screens.NewsPopup import NewsPopup
from ui.screens.InfoPopup import InfoPopup
from ui.screens.EventDecisionPopup import EventDecisionPopup
from ui.screens.EndGamePopup import EndGamePopup
from ui.screens.AlertPopup import AlertPopup
from ui.aspects.TextBox import create_text_box
# from ui.Screen import Screen
from ui.UIConstants import *
from ui.ScreenManager import ScreenManager

if __name__ == "__main__":
    # Init all of the pygame modules
    pygame.font.init()
    pygame.display.init()
    print("initialized font module!")

    # PYGAME CONSTANTS / Necessary Elements
    FPS = 60
    clock = pygame.time.Clock()
    mainloop = True
    playtime = 0.0

    # Set up the
    main_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    main_screen.blit(create_text_box("Loading...", 35, SCREEN_WIDTH, SCREEN_HEIGHT, (255, 255, 255), pygame.font.SysFont("Times New Roman", 50), True, True, False), (0, (4 * SCREEN_HEIGHT / 9)))
    pygame.display.flip()
    game_handler = GameHandler()
    main_menu = MainMenu(game_handler)
    screen_manager = ScreenManager(main_screen, main_menu)
    main_menu_node = screen_manager.screen_root_node
    game_screen = GameScreen(game_handler)
    game_screen_node = screen_manager.add_screen_to_current(game_screen)
    load_game_screen = LoadGameScreen(game_handler)
    screen_manager.add_screen_to_current(load_game_screen)
    screen_manager.screen_root_node.next_screen(1).add_screen(game_screen)
    credits_screen = CreditsScreen()
    screen_manager.add_screen_to_current(credits_screen)
    # game_screen_node = screen_manager.screen_root_node.next_screen(0)
    for place in game_handler.place_handler.places:
        place_screen = PlacePopup(place, game_handler)
        game_screen_node.add_screen(place_screen)
    money_popup = MoneyPopup(game_handler)
    game_screen_node.add_screen(money_popup)
    closeness_popup = ClosenessProgressBarsPopup(game_handler)
    game_screen_node.add_screen(closeness_popup)
    force_popup = ForceProgressBarsPopup(game_handler)
    game_screen_node.add_screen(force_popup)
    news_popup = NewsPopup(game_handler)
    game_screen_node.add_screen(news_popup)
    info_popup = InfoPopup()
    game_screen_node.add_screen(info_popup)
    settings_popup = SettingsPopup(game_handler)
    settings_popup_node = game_screen_node.add_screen(settings_popup)
    settings_popup_node.add_screen_node(main_menu_node)
    event_decision_popup = EventDecisionPopup(game_handler)
    game_screen_node.add_screen(event_decision_popup)
    end_game_popup = EndGamePopup(game_handler)
    end_game_popup_node = game_screen_node.add_screen(end_game_popup)
    end_game_popup_node.add_screen_node(main_menu_node)
    alert_popup = AlertPopup()
    game_screen_node.add_screen(alert_popup)

    while screen_manager.refresh():
        pass

    print("Thanks for playing!")

