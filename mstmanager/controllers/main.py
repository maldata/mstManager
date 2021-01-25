from PyQt5.QtCore import QObject, pyqtSlot, pyqtProperty, pyqtSignal

from mstmanager.controllers.screens.screen_info import ScreenInfo  ## , Screens
from mstmanager.controllers.screens.base_screen import BaseScreenController
from mstmanager.controllers.screens.screen_a import ScreenAController
from mstmanager.controllers.screens.screen_b import ScreenBController

import mstmanager.views.cliView
import mstmanager.dialogs.episodeentry
import mstmanager.dialogs.mediasetentry
import mstmanager.dialogs.addtocollection

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
        
    def startup(self):
        # self.view.init_ui()
        # self.view.addEpisodeEvent.subscribe(self.handle_add_episode_event)
        # self.view.addMediaSetEvent.subscribe(self.handle_add_media_set_event)
        # self.view.addToCollectionEvent.subscribe(self.handle_add_to_collection_event)
        # self.view.listSeasonEvent.subscribe(self.handle_list_season_event)
        # self.view.requestMediaSetUpdate.subscribe(self.handle_media_set_update_event)
        pass

    @pyqtSlot()
    def shutdown(self):
        self._app.quit()

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
    
    def run(self):
        self.view.run_ui()

    def deinitialize(self):
        pass

    def handle_add_episode_event(self):
        dlg = mstmanager.dialogs.episodeentry.EpisodeEntryController()
        result = dlg.get_episode_info()

        if result is not None:
            print('Adding {0}: {1}'.format(result.episode_number, result.title))
            self.db.add_episode(result.episode_number, result.title)
    
    def handle_add_media_set_event(self):
        dlg = mstmanager.dialogs.mediasetentry.MediaSetEntryController()
        result = dlg.get_media_set_name()

        if result is not None:
            print('Adding {0}'.format(result.media_set_name))
            self.db.add_media_set(result.media_set_name)
    
    def handle_add_to_collection_event(self):
        dlg = mstmanager.dialogs.addtocollection.AddToCollectionController(self.db)
        result = dlg.get_addition_info()
        
        if result is not None:
            e = result[0]
            m = result[1]
            print('Adding episode {0} to the collection as part of media set {1}'.format(e.episode_code, m.name))
            self.db.add_to_collection(e, m)

    def handle_list_season_event(self, season_code):
        episodes = self.db.get_episode_list_by_season(season_code)
        self.view.show_episodes_for_selected_season(episodes)
        
    def handle_media_set_update_event(self):
        self.view.all_media_sets = self.db.get_all_media_sets()
