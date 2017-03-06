import mstmanager.views.cliView
import mstmanager.dialogs.episodeentry
import mstmanager.dialogs.mediasetentry

class MainController:
    def __init__(self, db):
        self.view = mstmanager.views.cliView.CliView()
        self.db = db
        
    def initialize(self):
        self.view.init_ui()
        self.view.addEpisodeEvent.subscribe(self.handle_add_episode_event)
        self.view.addMediaSetEvent.subscribe(self.handle_add_media_set_event)
        self.view.addToCollectionEvent.subscribe(self.handle_add_to_collection_event)

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
        print('TODO: add to collection')
