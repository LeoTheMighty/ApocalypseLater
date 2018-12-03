from .Button import Button
from .Image import create_image
import os


class SpeedButton(Button):
    def __init__(self, identifier, rect):
        super().__init__(identifier, rect, os.path.join("img", "slow_forward.png"),
                         os.path.join("img", "regular_forward.png"),
                         os.path.join("img", "fast_forward.png"))
        self.slow_button_image = self.button_image
        self.regular_button_image = self.highlighted_button_image
        self.fast_button_image = self.pushed_button_image
        self.fastest_button_image = create_image(rect[2], rect[3], os.path.join("img", "fastest_forward.png"))
        self.highlighted_slow_button_image = create_image(rect[2], rect[3], os.path.join("img", "slow_forward_highlighted.png"))
        self.highlighted_regular_button_image = create_image(rect[2], rect[3], os.path.join("img", "regular_forward_highlighted.png"))
        self.highlighted_fast_button_image = create_image(rect[2], rect[3], os.path.join("img", "fast_forward_highlighted.png"))
        self.highlighted_fastest_button_image = create_image(rect[2], rect[3], os.path.join("img", "fastest_forward_highlighted.png"))
        self.pushed_slow_button_image = create_image(rect[2], rect[3], os.path.join("img", "slow_forward_pressed.png"))
        self.pushed_regular_button_image = create_image(rect[2], rect[3], os.path.join("img", "regular_forward_pressed.png"))
        self.pushed_fast_button_image = create_image(rect[2], rect[3], os.path.join("img", "fast_forward_pressed.png"))
        self.pushed_fastest_button_image = create_image(rect[2], rect[3], os.path.join("img", "fastest_forward_pressed.png"))
        self.speed_state = "regular"
        self.set_speed_state("regular")

    def set_speed_state(self, speed_state):
        if speed_state == "slow":
            self.speed_state = speed_state
            self.button_image = self.slow_button_image
            self.highlighted_button_image = self.highlighted_slow_button_image
            self.pushed_button_image = self.pushed_slow_button_image
        elif speed_state == "regular":
            self.speed_state = speed_state
            self.button_image = self.regular_button_image
            self.highlighted_button_image = self.highlighted_regular_button_image
            self.pushed_button_image = self.pushed_regular_button_image
        elif speed_state == "fast":
            self.speed_state = speed_state
            self.button_image = self.fast_button_image
            self.highlighted_button_image = self.highlighted_fast_button_image
            self.pushed_button_image = self.pushed_fast_button_image
        elif speed_state == "fastest":
            self.speed_state = speed_state
            self.button_image = self.fastest_button_image
            self.highlighted_button_image = self.highlighted_fastest_button_image
            self.pushed_button_image = self.pushed_fastest_button_image
        else:
            print("Unrecognized speed state = " + speed_state)

    def next_speed_state(self):
        if self.speed_state == "slow":
            self.set_speed_state("regular")
        elif self.speed_state == "regular":
            self.set_speed_state("fast")
        elif self.speed_state == "fast":
            self.set_speed_state("fastest")
        elif self.speed_state == "fastest":
            self.set_speed_state("slow")
