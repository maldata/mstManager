import mstmanager.views.cliView
import mstmanager.dialogs.episodeentry
import mstmanager.dialogs.mediasetentry
import mstmanager.dialogs.addtocollection

class MainController:
    def __init__(self, db):
        self.view = mstmanager.views.cliView.CliView()
        self.db = db
        
    def initialize(self):
        pass
#        self.view.init_ui()
#        self.view.addEpisodeEvent.subscribe(self.handle_add_episode_event)
#        self.view.addMediaSetEvent.subscribe(self.handle_add_media_set_event)
#        self.view.addToCollectionEvent.subscribe(self.handle_add_to_collection_event)
#        self.view.listSeasonEvent.subscribe(self.handle_list_season_event)
#        self.view.requestMediaSetUpdate.subscribe(self.handle_media_set_update_event)

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
