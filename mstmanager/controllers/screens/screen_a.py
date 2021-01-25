from .base_screen import BaseScreenController


class ScreenAController(BaseScreenController):
    def __init__(self):
        super().__init__()

    def initialize(self):
        print("Initializing screen A controller")

    def deinitialize(self):
        print("De-initializing screen A controller")
