from PyQt5.QtCore import QObject, pyqtSlot, pyqtProperty, pyqtSignal

from mstmanager.controllers.screens.screen_info import ScreenInfo
from mstmanager.controllers.screens.base_screen import BaseScreenController
from mstmanager.controllers.screens.screen_a import ScreenAController
from mstmanager.controllers.screens.screen_b import ScreenBController


class MainController(QObject):
    active_screen_changed = pyqtSignal()
    
    def __init__(self, app):
        super().__init__()

        self._app = app

        self._screen_map = {}
        self._screen_map["screen_a_key"] = ScreenInfo("screen_a_key",
                                                      './screens/screen_a.qml',
                                                      ScreenAController())
        self._screen_map["screen_b_key"] = ScreenInfo("screen_b_key",
                                                      './screens/screen_b.qml',
                                                      ScreenBController())
        
        self._active_screen_key = "screen_a_key"
        
    @pyqtProperty(str, notify=active_screen_changed)
    def active_screen_key(self):
        return self._active_screen_key

    @active_screen_key.setter
    def active_screen_key(self, value):
        if self._active_screen_key != value:
            self._active_screen_key = value
            self.active_screen_changed.emit()

    @pyqtProperty(str, notify=active_screen_changed)
    def active_screen_id(self):
        active_screen_info = self._screen_map[self.active_screen_key]
        return active_screen_info.id
    
    @pyqtProperty(str, notify=active_screen_changed)
    def active_screen_qml_path(self):
        active_screen_info = self._screen_map[self.active_screen_key]
        return active_screen_info.qml_path

    @pyqtProperty(str, notify=active_screen_changed)
    def active_screen_controller(self):
        active_screen_info = self._screen_map[self.active_screen_key]
        return active_screen_info.controller

    @pyqtSlot(str)
    def change_screen(self, next_screen_key):
        self.active_screen_controller.deinitialize()
        self.active_screen_key = next_screen_key
        self.active_screen_controller.initialize()
        self.active_screen_changed.emit()

    def startup(self):
        self.active_screen_controller.initialize()

    @pyqtSlot()
    def shutdown(self):
        self.active_screen_controller.deinitialize()
        self._app.quit()
