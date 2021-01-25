from .base_screen import BaseScreenController


class ScreenBController(BaseScreenController):
    def __init__(self):
        super().__init__()

    def initialize(self):
        print("Initializing screen B controller")

    def deinitialize(self):
        print("De-initializing screen B controller")
