from enum import Enum


class Screens(Enum):
    SCREEN_A = auto()
    SCREEN_B = auto()


class ScreenInfo:
    def __init__(self, screen_id, qml_path, controller):
        self._id = screen_id
        self._qml_path
        self._controller = controller

    @property
    def id(self):
        return self._id

    @property
    def qml_path(self):
        return self._qml_path

    @property
    def controller(self):
        return self._controller