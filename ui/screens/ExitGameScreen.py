from ..Popup import Popup
import os


class ExitGameScreen(Popup):
    def __init__(self):
        super().__init__(os.path.join("img", "red_granite.jpg"))
